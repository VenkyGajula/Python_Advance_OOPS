#Setter and Getters methods
#Setter Method :-We are set the values
#it is also known as mutator methods
""" Syntax:- def setVariables(self,variables):
                self.variable=variable
    Ex:- def setName(self,name):
                self.name=names"""
#Getter Methods
"""Getter methods can be used to get values of the instance variables. Getter methods also
known as accessor methods.
Syntax:
def getVariable(self):
 return self.variable
EX:- def getName(self):
        return self.name """

class Student :
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marls):
        self.marks=marks
    def getMarks(self):
        return self.marks
    def setRollno(self,rollno):
        self.rollno=rollno
    def getRollno(self):
        return self.rollno
n=int(input("Enter the number no of students : "))
for i in range(n) :
    s=Student()
    name=input("enter the name : ")
    s.setName(name)
    marks=int(input("Enter the marks"))
    s.setMarks(marks)
    rollno=int(input("Enter the Roll Number"))
    s.setRollno(rollno)

    print("Hi ",s.getName())
    print("Your Marks are :",s.getMarks())
    print("Your Roll Number :",s.getRollno())
    print()

print("*****Class Methods****")
class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs...".format(name,cls.legs))
Animal.walk("Dog")
Animal.walk("Cat")
Animal.walk("Lion")
Animal.walk("Tiger")

print("****static Methods*****")
class SM:

    @staticmethod
    def add(x,y):
        print("Thes sum :",x+y)
    @staticmethod
    def product(x,y):
        print("Thes product :",x*y)
    @staticmethod
    def sub(x,y):
        print("Thes sub :",x-y)
    @staticmethod
    def average(x,y):
        print("Thes Average :",(x+y)/2)
SM.add(2,5)
SM.sub(10,5)
SM.product(5,5)
SM.average(55,10)
