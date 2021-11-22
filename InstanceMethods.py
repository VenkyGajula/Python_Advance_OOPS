#Instance methods
class Student:

    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("Your Roll Numbetr :",self.rollno)
        print("Hi :",self.name)
        print("Your Marks :",self.marks)
    def grade(self):
        if self.marks>=85:
            print("Your Roll Number is :",rollno)
            print("Your grade is : O")
        elif self.marks>=60:
            print("Your Roll Number is :",rollno)
            print("Your grade is : A")
        elif self.marks>=50:
            print("Your Roll Number is :",rollno)
            print("Your grade is : B")
        elif self.marks>=35:
            print("Your Roll Number is :",rollno)
            print("Your grade is : C")
        else :
            print("Your Roll Number is :",rollno)
            print("Your Failed")
n=int(input("Enter number of Students :"))
for i in range(n):
    name=input("Enter the Name :")
    rollno=int(input("Enter the Roll NUmber :"))
    marks=int(input("Enter teh MArks :"))
    s=Student(name,rollno,marks)
    s.display()
    s.grade()
    print()
