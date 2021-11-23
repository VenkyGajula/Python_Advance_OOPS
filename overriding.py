#3)Overriding
print("****Method Overriding*****")
"""What ever members available in the parent class are bydefault available to the child
class through inheritance. If the child class not satisfied with parent class
implementation then child class is allowed to redefine that method in the child class
based on its requirement. This concept is called overriding.
--->Overriding concept applicable for both methods and constructors. """
class P:
    def property(self):
        print("Gold+Land+Cash")
    def marry(self):
        print("AMB")
class C(P):
    def marry(self):
        print("Arr")

c=C()
c.property()
c.marry()

print("***Constructor Overriding*****")
class Father:
    def __init__(self):
        print("Father Constructor")
class Me(Father):
    def __init__(self):
        print("My constructor")
m=Me()

print("***to call Parent Class Constructor by using super()*****")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def display(self):
        print("Emp name : ",self.name)
        print("Emp Age : ",self.age)
        print("Emp eno : ",self.eno)
        print("Emp esal : ",self.esal)

e=Employee("venky",24,101,55000)
e.display()
print("\n")
e1=Employee("Ravi",25,102,60000)
e1.display()
print("\n")
e2=Employee("Hari",26,103,50000)
e2.display()
