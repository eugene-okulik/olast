INSERT INTO `students` (name, second_name, group_id) VALUES ('Olesya', 'Test', 3024)

INSERT INTO books (title, taken_by_student_id) VALUES ('QA Python', 4680), ('QA QA', 4680), ('SQL QA QA', 4680)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('test sql', 'march 2024', 'june 2024')

INSERT INTO subjets (title) VALUES ('Math QA'), ('Chemistry'), ('Physics')

INSERT INTO lessons (title, subject_id) VALUES
('math lesson one', 4872), ('math lesson two', 4872),
('chemistry lesson one', 4873), ('chemistry lesson two', 4873),
('physics lesson one', 4874), ('physics lesson two', 4874)

INSERT INTO marks (value, lesson_id, student_id) VALUES
(4, 8866, 4680), (3, 8867, 4680),
(5, 8868, 4680), (5, 8869, 4680),
(3, 8870, 4680), (4, 8871, 4680)

SELECT * FROM marks where student_id = 4680

SELECT * FROM books where taken_by_student_id = 4680

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
WHERE s.id = 4680
GROUP BY s.id, s.name, s.second_name, g.title, l.title, s2.title, m.value
ORDER BY l.title;