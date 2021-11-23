#OverLoading:-We can use same operator or methods for different purposes
""" There are 3 types of Overloading
1) Operator Overloading
2) Method Overloading
3) Constructor Overloading """

print("***1.Operatorm OverLoading****")
#We can use the same operator for multiple purposes, which is nothing but operator overloading.
#--> Python supports operator overloading.
class Book:
    def __init__(self,pages):
          self.pages=pages
    def add(self,other):
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)
#print("Total Pages :",b1+b2)

#2)Method Overriding:-
"""If 2 methods having same name but different type of arguments then those methods
are said to be overloaded methods.
 Eg: m1(int a)
 m1(double d)
--> But in Python Method overloading is not possible.
-->If we are trying to declare multiple methods with same name and different number of
arguments then Python will always consider only last method. """

print("*****Method Overloading*****")
class Test:
    def m1(self):
        print('no-arg method')
    def m1(self,a):
        print('one-arg method')
    def m1(self,a,b):
        print('two-arg method')
t=Test()
#t.m1()
#t.m1(10)
t.m1(10,20)

#3).Constructor Overloading:--
"""Constructor overloading is not possible in Python.
--> If we define multiple constructors then the last constructor will be considered."""
print("*****constructorOverloading*****")
class Sample:
    def __init__(self):
         print('No-Arg Constructor')
    def __init__(self):
        print("1--Arg Constructor")
    def __init__(self,a,b):
        print("2--Arg constructor")
#s1=Sample()
#s1=Sample(10)
s1=Sample(10,20)
