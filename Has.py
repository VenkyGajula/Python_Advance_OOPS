#Inheritance
#USing Members of One Class inside Another Class:
#we can use members of one class inside another class by using the following always
#1).By Composition(Has-A Relationship)
#2)BY Inheritance(Is-A Relationship)

#1)BY Composition(HAs-A Relationship)
"""By using Class Name or by creating object we can access members of one class inside
another class is nothing but composition (Has-A Relationship).
---->The main advantage of Has-A Relationship is Code Reusability.
print("****Demo Program******")
class Engine:
  a=10
  def __init__(self,b):
    self.b=20
  def m1(self):
    print("Engine specific Functionalities")
class Car:
    def __inir__(self):
      sel.engine=Engine()
    def m2(self):
      print("Car using Engine class Functionalities")
      print(self.engine.a)
      print(self.engine.b)
      self.engine.m1()
c=Car()
c.m2()"""


print("***Demo Program 2******")
class Bus:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def busInfo(self):
        print("BusName:{},Model:{},color:{}".format(self.name,self.model,self.color))
class Emp:
    def __init__(self,ename,eid,bus):
        self.ename=ename
        self.eid=eid
        self.bus=bus
    def empInfo(self):
        print("Employee Name :",self.ename)
        print("Employee id : ",self.eid)
        print("Employee bus :",self.bus)

b=Bus("Asoka","2015AS","Yellow")
e=Emp("Venky",101,b)
e.empInfo()
