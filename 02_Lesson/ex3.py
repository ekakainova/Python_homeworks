from student import Student
from CourseGroup import CourseGroup

student1 = Student('Андрей', 'Иванов', 22, 'Программирование')
classmate1 = Student('Марина', 'Казакова', 23, 'Программирование')
classmate2 = Student('Михаил', 'Логинов', 21, 'Программирование')

course_group = CourseGroup(student1, [classmate1, classmate2])

print(course_group)