class Student:
    native_pace = 'Espoo'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender  # age don't want use outside
        print('init method')

    def eat(self):
        print('eat method')
        print(self.name + ' eat ')

    def display(self):
        print(self.name, self.age, self.__gender)

    @staticmethod
    def method():
        print('static method')

    @classmethod
    def cm(cls):
        print('class method')


print(Student)
print(id(Student))
print(type(Student))
stu1 = Student('zhangsan', 20, 'male')
stu2 = Student('lisi', 30, 'female')
print(stu1)
print(id(stu1))
print(type(stu1))
stu1.eat()  # object.method
print(stu1.name)
print(stu1.age)
print('-------------------------')
Student.eat(stu1)  # class.method

print(Student.native_pace)
print(stu1.native_pace)
print(stu2.native_pace)
print('-------------------------')
Student.native_pace = 'Helsinki'
print(stu1.native_pace)
print(stu2.native_pace)

print('-------------------------')
Student.cm()
Student.method()
Student.eat(stu2)
print('------------dynamic attribute-------------')
stu2.phone = '123456'
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.phone)
print('------------dynamic method-------------')


def show():
    print('show method out of class')


stu1.show = show
stu1.show()

stu1.display()
# print(stu1.__gender) # no attribute
print(dir(stu1))
print(stu1._Student__gender) # access by _Student__age

