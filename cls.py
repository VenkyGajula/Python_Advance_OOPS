print("****OPPS****")
#Class :- In python every thing is an object. To create Object we required some Model or Plan or Blue print, Which is nothing but Class
#class className:
#class Person:
 # """ This is person details"""
#print(Person.__dict__)
#help(Person)"""
#Three types of variables are there
"""1.Instance Variable(Object Level Variable)
   2.Static Variable(Class Level VAriable)
   3.Local VAriable(Method Level Variable)
   Three Types of Methods is there
   1.Instance Methods
   2.Class Methods
   3.Static Methods"""
#Ex:- Class
class Student:

    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def info(self):
        print("Hello Iam :",self.name)
        print("MY age is :",self.age)
        print("My marks are :",self.marks)


s1=Student("Venky",24,85)
s1.info()
