# words = 'Hello world'
# Split_words = words.split(' ')
# joined_words = '*'.join(Split_words)
# print(Split_words)
# print(joined_words)
# name = 'Alice'
# age = 25
# F_string = f'Hello, {name}. You are {age} years old.'
# print(F_string)


class Person:
    def __init__(self,name,age,id):
     self.name = name
     self.age = age
     self.id = id
    def introduce(self):
       print(f'My name is {self.name}. I am {self.age} years old, my ID is {self.id}')
       

# person = Person('Alex', 30, "007")
# person.introduce()

class Student(Person):
   def study(self):
      print(f'{self.name} is studying.')

class Teacher(Person):
    def teach(self):
        print(f'{self.name} is teaching.')

Student = Student("Alex", 30, "007")
Student.study()

teacher = Teacher("Ben", 80, "24")
teacher.teach()