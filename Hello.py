class Intro:
  def __init__(self,name,age):
     self.name = name
     self.age = age
  def __repr__(self):
    return f"Name:{self.name},Age:{self.age} "
     
     
person1  = Intro('Aegon',565)

print(person1)
