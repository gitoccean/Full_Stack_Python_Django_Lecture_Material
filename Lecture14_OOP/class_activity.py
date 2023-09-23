class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_student_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Grade: {self.grade}')

    def is_passing(self):
        return self.grade >= 40

    def promote(self):
        if self.grade < 100:
            self.grade += 10
            print(f'{self.name} has been promoted to the next grade')
        else:
            print(f'{self.name} has already reached the highest grade')

student1 = Student('Mohtashim', 19, 75)
student2 = Student('Abubaker', 22, 100)

print('Student 2 Information')
student2.display_student_info()

print('Student 2 is Passing?', student2.is_passing())

student2.promote()
