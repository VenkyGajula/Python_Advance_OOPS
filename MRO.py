#Method Resolution Order(MRO):
"""In Hybrid Inheritance the method resolution order is decided based on MRO
algorithm.
-->This algorithm is also known as C3 algorithm.
-->Samuele Pedroni proposed this algorithm.
-->It follows DLR (Depth First Left to Right) i.e Child will get more priority than Parent.
-->Left Parent will get more priority than Right Parent.
-->MRO(X) = X+Merge(MRO(P1),MRO(P2),...,ParentList)

Head Element vs Tail Terminology:
-->Assume C1,C2,C3,...are classes.
-->In the list: C1C2C3C4C5....
-->C1 is considered as Head Element and remaining is considered as Tail.

How to find Merge:
-->Take the head of first list
-->If the head is not in the tail part of any other list, then add this head to the result and
remove it from the lists in the merge.
-->If the head is present in the tail part of any other list, then consider the head element
of the next list and continue the same process.

Note: We can find MRO of any class by using mro() function.
 print(ClassName.mro())
"""

print("****Demo Program-1 for Method Resolution Order*********")
class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
