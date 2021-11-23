#Hierarchical INheritance
""" The concept of inheriting properties from one class into multiple classes which are
present at same level is known as Hierarchical Inheritance
EX:-- parent--->c1,parent---->c2 """
print("***Hierarchical Inheritance****")
class A:
    a=20
    b=10
    def m1(self):
        print("PArent METHOD")
class B(A):
    def m2(self):
        print("Child class---1")
class C(A):
    def m3(self):
        print("child class---2")
class D(A):
    def m4(self):
        print("child class--3")
b=B()
b.m1()
print(b.a)
print(b.b)
b.m2()
c=C()
c.m1()
print(c.a)
print(c.b)
c.m3()
d=D()
d.m1()
print(d.a)
print(d.b)
d.m4()
