#Types of inheritance
print("****Single-level Inheritance***")
""" To acquiringthe properties and behaviors from one class to another class
Ex:- A(p,b)-->B,Parent(p,b)---->child """
class A:
  def m1(self):
    print("Parent method")
class B(A):
  def m2(self):
    print("child method")
b=B()
b.m1()
b.m2()

print("**********")
class P:
    a=10
    b=20
    def info(self):
        print("Parent class method")
class C(P):
    def information(self):
        print("Child class method")
c=C()
print(c.a)
print(c.b)
c.info()
c.information()
