#Object Orientated Programming 

class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class course:
    def __init__(self, name,max_students):
        self.name = names
        self.max_students = max_students
        self.student = []

    def add_student(self, student):
        if len(self.student) < self.max_students:
            self.student.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()

        return value / len(self.student)

s1 = student("tim", 19, 99)
s2 = student("tim", 19, 75)
s3 = student("tim", 19, 69)

course = course("science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.student[0].name)