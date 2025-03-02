INSERT INTO `students` (name, second_name) VALUES ('Olesya', 'Testovna')

INSERT books (title, taken_by_student_id) VALUES ('QA Manual', 4704), ('QA-QA', 4704), ('SQL Learn', 4704)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('test sql 2', 'march 2024', 'july 2024')

UPDATE `students` SET group_id = 3048 WHERE id = 4704;

INSERT INTO subjets (title) VALUES ('Math QA Auto'), ('Chemistry Auto'), ('Physics Auto')

INSERT INTO lessons (title, subject_id) VALUES
('math QA lesson one', 4917), ('math QA lesson two', 4917),
('chemistry QA lesson one', 4918), ('chemistry QA lesson two', 4918),
('physics QA lesson one', 4919), ('physics QA lesson two', 4919)

INSERT INTO marks (value, lesson_id, student_id) VALUES
(4, 8918, 4704), (3, 8919, 4704),
(5, 8920, 4704), (5, 8921, 4704),
(3, 8922, 4704), (4, 8923, 4704)

SELECT * FROM marks where student_id = 4704

SELECT * FROM books where taken_by_student_id = 4704

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
WHERE s.id = 4704
GROUP BY s.id, s.name, s.second_name, g.title, l.title, s2.title, m.value
ORDER BY l.title;