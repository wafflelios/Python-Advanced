select avg(grade)
from assignments_grades
join assignments on assignments_grades.assisgnment_id = assignments.assisgnment_id
where assignments.assignment_text like '%прочитать%' or assignments.assignment_text like '%выучить%';
