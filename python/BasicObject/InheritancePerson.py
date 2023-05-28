class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no


class Teacher(Person):
    def __init__(self, name, age, tech_year):
        super().__init__(name, age)
        self.tech_year = tech_year


stu = Student('zhangsan', 20, '1001')
teacher = Teacher('lisi', 40, 15)
stu.info()  # come form Person
teacher.info()  # come form Person
