select count(distinct students.student_id) as students_amount,
       avg(assignments_grades.grade) as avg_grade,
       count(distinct case when assignments_grades.grade is null then students.student_id end) as no_word_found,
       count(distinct case when assignments_grades.grade > assignments.due_date then students.student_id end) as after_deadline,
       count(distinct assignments_grades.grade_id) as second_try
from students
left join assignments_grades on students.student_id = assignments_grades.student_id
left join assignments on assignments.assisgnment_id = assignments_grades.assisgnment_id
group by students.group_id;
