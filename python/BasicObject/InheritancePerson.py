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

    def info(self):  # method overload
        super().info()
        print('student no: ',self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, teach_year):
        super().__init__(name, age)
        self.teach_year = teach_year

    def info(self):  # method overload
        super().info()
        print('teach_year: ',self.teach_year)


stu = Student('zhangsan', 20, '1001')
teacher = Teacher('lisi', 40, 15)
stu.info()  # come form Person
teacher.info()  # come form Person
