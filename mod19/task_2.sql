select full_name as student_name, avg(assignments_grades.grade) as avg_grade
from students
join assignments_grades on students.student_id = assignments_grades.student_id
group by full_name
order by avg_grade desc
limit 10;