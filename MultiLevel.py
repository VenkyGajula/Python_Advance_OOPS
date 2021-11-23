#multi-level inheritance
"""The concept of inheriting the properties from multiple classes to single class with the
concept of one after another is known as multilevel inheritance
Ex:-- GandFather--->Father--->Father  """

print("*****Multi Level INheritance*****")
class P:
  def m1(self):
    print("Parent Method")
class C(P):
  def m2(self):
    print("Child Method")
class CC(C):
  def m3(self):
      print("Sub Child Method")
c=CC()
c.m1()
c.m2()
c.m3()

print("******")
class Gf:
    def properties(self):
        print("10 shops")
class F(Gf):
    def pro(self):
        print("8 shops")
class Me(F):
    def pr(self):
        print("5 shops")
print("my total shops")

m=Me()
m.properties()
m.pro()
m.pr()
print("total shopes: ",10+8+5)
