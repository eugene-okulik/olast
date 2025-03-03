import dotenv
import pymysql
import os
import csv

dotenv.load_dotenv()
db = pymysql.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

try:
    cursor = db.cursor(pymysql.cursors.DictCursor)

    query = """
        SELECT
            st.id AS student_id,
            st.name AS student_name,
            st.second_name AS student_second_name,
            g.title AS group_title,
            b.title AS book_title,
            m.value AS mark_value,
            l.title AS lesson_title,
            sj.title AS subject_title
        FROM students st
        LEFT JOIN books b ON st.id = b.taken_by_student_id
        LEFT JOIN `groups` g ON st.group_id = g.id
        LEFT JOIN marks m ON st.id = m.student_id
        LEFT JOIN lessons l ON l.id = m.lesson_id
        LEFT JOIN subjets sj ON sj.id = l.subject_id
    """
    cursor.execute(query)
    student_info = cursor.fetchall()

    file = 'data.csv'
    base_path = os.path.dirname(__file__)
    homework_path = os.path.dirname(os.path.dirname(os.path.dirname(base_path)))
    new_file_path = os.path.join(
        homework_path, 'homework', 'eugene_okulik', 'Lesson_16', 'hw_data', file
    )

    with open(new_file_path, newline='', encoding='utf-8') as csv_new:
        reader = csv.DictReader(csv_new)
        csv_data = [row for row in reader]

    missing_data = []

    for csv_row in csv_data:
        name = csv_row['name']
        second_name = csv_row['second_name']
        group_title = csv_row['group_title']
        book_title = csv_row['book_title']
        subject_title = csv_row['subject_title']
        lesson_title = csv_row['lesson_title']
        mark_value = csv_row['mark_value']

        found_in_base = False
        for base_row in student_info:
            if (base_row['student_name'] == name
                    and base_row['student_second_name'] == second_name
                    and base_row['group_title'] == group_title
                    and base_row['book_title'] == book_title
                    and base_row['subject_title'] == subject_title
                    and base_row['lesson_title'] == lesson_title
                    and str(base_row['mark_value']) == mark_value):
                found_in_base = True
                break

        if not found_in_base:
            missing_data.append({
                'name': name,
                'second_name': second_name,
                'group_title': group_title,
                'book_title': book_title,
                'subject_title': subject_title,
                'lesson_title': lesson_title,
                'mark_value': mark_value
            })

    if missing_data:
        print("Недостающие записи в базе данных:")
        for data in missing_data:
            print(
                f"name: {data['name']}, "
                f"second_name: {data['second_name']}, "
                f"group_title: {data['group_title']}, "
                f"book_title: {data['book_title']}, "
                f"subject_title: {data['subject_title']}, "
                f"lesson_title: {data['lesson_title']}, "
                f"mark_value: {data['mark_value']}"
            )
    else:
        print("Все записи из csv файла есть в базе данных.")

finally:
    cursor.close()
    db.close()
