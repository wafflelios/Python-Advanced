select full_name as  teacher_name, avg(assignments_grades.grade) as avg_grade
from teachers
join assignments on teachers.teacher_id = assignments.teacher_id
join assignments_grades on assignments.assisgnment_id = assignments_grades.assisgnment_id
group by full_name
order by avg_grade
limit 1;