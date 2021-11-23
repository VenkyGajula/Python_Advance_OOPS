#Inheritance Is-A Relationship
print("*** By Inheritance (IS-A Relationship)****")
"""What ever variables, methods and constructors available in the parent class by default
available to the child classes and we are not required to rewrite. Hence the main
advantage of inheritance is Code Reusability and we can extend existing functionality
with some more extra functionality.
Syntax:--class childclass(parentclass) """

class Parent:
    a=10
    def __init__(self):
        self.b=10
    def m1(self):
        print("Parent Instance Method")
    @classmethod
    def m2(cls):
        print("PArent class method")
    @staticmethod
    def m3():
        print("parent static method")

class Child(Parent):
    pass

c=Child()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()

print("****")
class P:
    def m4(self):
        print("Parent class method")

class C(P):
    def m5(self):
        print("child class method")
c=C()
c.m4()
c.m5()

print("********")
class Pa:
    a=10
    def __init__(self):
        self.b=20
class Ch(Pa):
    c=30
    def __init__(self):
        super().__init__()
        self.d=30

c1=Ch()
print(c1.a,c1.b,c1.c,c1.d)

print("****Demo Program for Inheritance*****")
class Human:
    def __init__(self,name,age,color):
            self.name=name
            self.age=age
            self.color=color
    def activities(self):
        print("Eating")
        print("Drinking")
        print("Sleeping")
        print("Dancing")
class Employee(Human):
    def __init__(self,name,age,color,eno,esal):
        super().__init__(name,age,color)
        self.eno=eno
        self.esal=esal

    def work(self):
        print("Python is very easy")
    def eInfo(self):
        print("Empoyee Name : ",self.name)
        print("Employee Age : ",self.age)
        print("Employee Color : ",self.color)
        print("Employee eno : ",self.eno)
        print("Employee salary : ",self.esal)

e=Employee("Venkatesh",24,"black",101,55000)
e.eInfo()
e.activities()
e.work()
