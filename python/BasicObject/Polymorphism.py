class Animal(object):
    def eat(self):
        print('Animal will eat')


class Dog(Animal):
    def eat(self):
        print('Dog eat bone')


class Cat(Animal):
    def eat(self):
        print('Cat eat fish')


class Person:
    def eat(self):
        print('Person eat food')


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())
