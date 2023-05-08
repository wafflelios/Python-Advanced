select group_id, min(count_grade) as min, max(count_grade) as max, avg(count_grade) as avg
from (select group_id, count(grade) as count_grade
      from students
      join assignments_grades on students.student_id = assignments_grades.student_id
      where grade = 0
      group by students.student_id, group_id)
group by  group_id
