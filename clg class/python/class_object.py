#pythpn classes and objects
class MyClass:
  x = 5
  y=10
  z=x+y
p1 = MyClass()
print(p1.z)

#function inside class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person("John", 36)
# print(p2.name)

class Car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def myfunc(self):
    print(f"I have a {self.brand} {self.model}")

c1=Car("BMW","X5")
c1.myfunc()