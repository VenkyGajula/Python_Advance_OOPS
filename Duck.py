#polymarphism
""" Polymarphism is a greek word,poly means many, marphism means forms.
Polymorphism means 'Many Forms'.
Related to Polymorphism the following 4 topics are important:
1) Duck Typing Philosophy of Python
2) Overloading
    1) Operator Overloading
    2) Method Overloading
    3) Constructor Overloading
3) Overriding
    1) Method Overriding
    2) Constructor Overriding.  """


print("***Duck Typing Philosophy of Python***")
class Duck:
    def talk(self):
      print('Quack.. Quack..')

class Dog:
  def talk(self):
    print('Bow Bow..')
class Cat:
  def talk(self):
    print('Moew Moew ..')
class Goat:
  def talk(self):
    print('Myaah Myaah ..')
  def f1(obj):
    obj.talk()

l=[Duck(),Cat(),Dog(),Goat()]
for obj in l:
    f1(obj)
