#Inside constructor by using self variables
class Emp:
    def __init__(self):
        self.eno=101
        self.eName="venky"
        self.eSal=50000
#Inside Instance Method By using Self VAriable
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
e=Emp()
e.m1()
print(e.__dict__)

#Outside of the Class by using Object Reference Variable
e.d=40
print(e.__dict__)

#Delete Instance Variable from the object
    #def m2(self):
    #    del self.c
#e.m2()
print(e.__dict__)
#e.m2()
del e.d
print(e.__dict__)

#Static variables
