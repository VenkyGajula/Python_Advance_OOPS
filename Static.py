#Static variables
"""If the value of a variable is not varied from object to object, such type of variables we
have to declare with in the class directly but outside of methods. Such types of
variables are called Static variables"""
class Sample :
  x=20
  def __init__(self):
       self.y=30
s1=Sample()
s2=Sample()
print("s1 :",s1.x,s1.y)
print("s2 :",s2.x,s2.y)
print(Sample.x)
Sample.x=555
s1.y=444
print("s1 :",s1.x,s1.y)
print("s2 :",s2.x,s2.y)

#Where we can modify the Value of Static Variable
"""Anywhere either with in the class or outside of class we can modify by using classname.
But inside class method, by using cls variable.
    def __m1__(cls):
        cls.x=888
    #static methods
    def __m2__():
        Sample.x=999
s3=Sample()
print(Sample.x)
Sample.m1()
print(Sample.x)
Sample.m2()
print(Sample.x)"""

#How to Delete Static Variables of a Class

"""1) We can delete static variables from anywhere by using the following syntax
   ""del classname.variablename""
2) But inside classmethod we can also use cls variable
 ""del cls.variablename"""

class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=30
        del Test.b
    @classmethod 
    def m2(cls):
        cls.d=40
        del Test.c
    @staticmethod
    def m3():
        Test.e=50
        del Test.d
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f=60
print(Test.__dict__)
del Test.e
print(Test.__dict__)
