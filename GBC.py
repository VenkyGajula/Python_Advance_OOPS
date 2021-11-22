print("****Garbage Collection*****")
#How to enable and disable Garbage Collector in our Program :
"""1) gc.isenabled()  Returns True if GC enabled
   2) gc.disable() To disable GC explicitly
   3) gc.enable() To enable GC explicitly """

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

print("*****Destructors*****")
"""Destructor is a special method and the name should be __del__
--> Just before destroying an object Garbage Collector always calls destructor to perform
clean up activities (Resource deallocation activities like close database connection etc).
--->Once destructor execution completed then Garbage Collector automatically destroys
that object. """

import time
class Test:
    def __init__(self):
        print("Object Initialization...")
    def __del__(self):
        print("Fulfilling Last Wish and performing clean up activities...")
t1=Test()
t1=None
time.sleep(5)
print("End of application")


print("****find the Number of References of an Object****")
"""sys module contains getrefcount() function for this purpose.
sys.getrefcount (objectreference) """
import sys
class Sample:
    pass
s1=Sample()
s2=s1
s3=s1
s4=s1
s5=s1
print(sys.getrefcount(s1))
