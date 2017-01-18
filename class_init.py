class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade

law = Student('Law', 85, 24)
dan = Student('Dan', 95, 25)

print(law.name)
print(law.grade)
print(law.age)

print(dan.name)
print(dan.grade)
print(dan.age)
