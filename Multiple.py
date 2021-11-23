#multiple INheritance
""" The concept of inheriting the properties from multiple classes into a single class at a
time, is known as multiple inheritance
EX:--p1---->c,p2---->c """
print("****Multiple Inheritance****")
class P1:
  def m1(self):
    print("Parent1 Method")
class P2:
  def m2(self):
    print("Parent2 Method")
class C(P1,P2):
  def m3(self):
    print("Child Method")
c=C()
c.m1()
c.m2()
c.m3()

print("***********")
"""Hybrid Inheritance :--Combination of Single, Multi level, multiple and Hierarchical inheritance is known as
Hybrid Inheritance. """

print("***********")
#Cyclic INheritance
""" The concept of inheriting properties from one class to another class in cyclic way, is
called Cyclic inheritance.Python won't support for Cyclic Inheritance of course it is
really not required.
EX:-
class A(B):
    pass
class B(A):
    pass
NameError: name 'B' is not defined

"""
