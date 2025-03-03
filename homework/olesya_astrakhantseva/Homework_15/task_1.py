import pymysql

db = pymysql.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(pymysql.cursors.DictCursor)

# Создание студента без группы
insert_new_student = """
INSERT INTO students (name, second_name)
VALUES (%s, %s)
"""
cursor.execute(insert_new_student, ('Olesya', 'Pycharm'))
student_id = cursor.lastrowid
print(f"Создан студент с id: {student_id}")

# Создание группы
insert_group = """
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s)
"""
cursor.execute(insert_group, ('TEST SQL PYCHARM', '2025-03-01', '2025-07-31'))
group_id = cursor.lastrowid
print(f"Создана группа с id: {group_id}")


# Добавление студента в группу
insert_student_in_group = """
UPDATE `students` SET group_id = %s WHERE id = %s
"""
cursor.execute(insert_student_in_group, (group_id, student_id))
print(f"Студент {student_id} добавлен в группу {group_id}")

# Создание учебников
insert_books = """
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
"""
values_books = [
    ('QA Pycharm', student_id),
    ('QA SQL', student_id),
    ('QA BD', student_id)
]

books_created = []
for book in values_books:
    cursor.execute(insert_books, book)
    last_id_book = cursor.lastrowid
    books_created.append(last_id_book)
print(f"Книги с ID {', '.join(map(str, books_created))} были созданы")

# Создание предметов
insert_subjects = """
INSERT INTO subjets (title)
VALUES (%s)
"""
subjects_values = [
    'QA Auto Math',
    'QA Auto Chemistry',
    'QA Auto Physics'
]
subjects_created = []
for subject in subjects_values:
    cursor.execute(insert_subjects, subject)
    last_id_subject = cursor.lastrowid
    subjects_created.append(last_id_subject)

subj1, subj2, subj3 = (
    subjects_created[0],
    subjects_created[1],
    subjects_created[2]
)
print(f"Предметы с ID {', '.join(map(str, subjects_created))} были созданы")

# Создание уроков
insert_lessons = """
INSERT INTO lessons (title, subject_id)
VALUES (%s, %s)
"""
values_lessons = [
    ('Monday QA', subj1),
    ('Tuesday QA', subj1),
    ('Wednesday QA', subj2),
    ('Thursday QA', subj2),
    ('Friday QA', subj3),
    ('Saturday QA', subj3)
]
lessons_created = []
for lesson in values_lessons:
    cursor.execute(insert_lessons, lesson)
    last_id_lessons = cursor.lastrowid
    lessons_created.append(last_id_lessons)
print(f"Уроки с id {', '.join(map(str, lessons_created))} были созданы")

# Создание оценок
insert_marks = ("INSERT INTO marks (value, lesson_id, student_id)"
                " VALUES (%s, %s, %s)")
values_marks = [
    (5, lessons_created[0], student_id),
    (4, lessons_created[1], student_id),
    (3, lessons_created[2], student_id),
    (5, lessons_created[3], student_id),
    (4, lessons_created[4], student_id),
    (3, lessons_created[5], student_id)
]
marks_created = []
for mark in values_marks:
    cursor.execute(insert_marks, mark)
    last_id_marks = cursor.lastrowid
    marks_created.append(last_id_marks)
print(f"Оценки с id {', '.join(map(str, marks_created))} были созданы")

# Получение всех оценок студента
cursor.execute("SELECT value FROM marks m WHERE student_id = %s",
               (student_id,))
marks_data = cursor.fetchall()
marks = [mark['value'] for mark in marks_data]
print(f"Студент с ID {student_id} имеет оценки: {', '.join(map(str, marks))}")

# Получение всех книг, которые находятся у студента
cursor.execute(
    "SELECT * FROM books WHERE taken_by_student_id = %s",
    (student_id,)
)
books_data = cursor.fetchall()
books = [book['title'] for book in books_data]
print(f"Студент с ID {student_id} взял книги: {', '.join(books)}")

# Получение всей информации о студенте
student_info = """
    SELECT
        s.id AS student_id,
        s.name AS student_name,
        s.second_name AS student_second_name,
        g.title AS group_title,
        GROUP_CONCAT(DISTINCT b.title SEPARATOR ', ') AS books_taken,
        l.title AS lesson_title,
        s2.title AS subject_title,
        m.value AS mark
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON b.taken_by_student_id = s.id
    LEFT JOIN marks m ON m.student_id = s.id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjets s2 ON l.subject_id = s2.id
    WHERE s.id = %s
    GROUP BY s.id, s.name, s.second_name, g.title, l.title, s2.title, m.value
    ORDER BY l.title;
"""
cursor.execute(student_info, (student_id,))
student_info = cursor.fetchall()
print(f'Информация о студенте с id: {student_id}: ',
      *student_info, sep="\n")

db.commit()
cursor.close()
db.close()
