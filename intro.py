class Person(object):
  def __init__(self, name, age): #
    self.name = name
    self.age = age
    
  def get_person(self):
    return "<Person (%, %)>".format(self.name, self.age)
    
