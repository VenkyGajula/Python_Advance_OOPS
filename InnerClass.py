print("****Inner Classes*****")
#With in class we are creating another classes is called Inner Classes.
class Outer:
    def __init__(self):
        print("Outer class Object Creation")
    class Inner:
        def __init__(self):
            print("inner class object creation")
        def m1(self):
            print("inner clASS METHOD")
o=Outer()
i=o.Inner()
i.m1()

class Person:
    def __init__(self):
        self.name="venky"
        self.dob=self.Dob()
    def display(self):
        print("Name :",self.name)
    class Dob:
        def __init__(self):
            self.dd=1
            self.mm=1
            self.year=1997
        def displays(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.year))
p=Person()
p.display()
i=p.Dob()
i.displays()
