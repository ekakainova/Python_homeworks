class Student:

    def __init__(self, firstName, lastName, age, course):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.course = course

    def __str__(self):
        return f'{self.firstName} {self.lastName}, {self.age} года, курс: {self.course}'