class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        #self.is_active = False
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade() 
        return value / len(self.students)


s1 = Student("Daniel", 20, 18)
s2 = Student("Carlos", 40, 82)
s3 = Student("José", 25, 15)

courseScience = Course("Science", 2)
courseScience.add_student(s1)
courseScience.add_student(s2)
 
print(courseScience.students[0].get_name())
print(courseScience.get_average_grade())

 