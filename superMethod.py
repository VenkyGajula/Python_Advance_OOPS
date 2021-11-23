#super() METHOD
"""super() is a built-in method which is useful to call the super class constructors,variables
and methods from the child class"""
print("********")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        super().display()
        print('Roll No:',self.rollno)
        print('Marks:',self.marks)
s1=Student('venky',22,101,90)
s1.display()

print("************")
class P:
    a=10
    def __init__(self):
        self.b=10
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P): 
    a=888
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
c=C()
