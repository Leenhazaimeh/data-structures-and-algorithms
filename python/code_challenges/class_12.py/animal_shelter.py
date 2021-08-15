from new_qeue import *

class AnimalShelter:
  def __init__(self) :
      self.cat=Queue()
      self.dog=Queue()

  def enqueue(self,animal):
      if animal=='cat' :
        self.cat.enqueue(animal)
      
      elif animal=='dog' :
        self.dog.enqueue(animal)

      else :
        return 'not in the list'
   

  def dequeue(self,animal):
    if animal =='cat' and self.cat.front:
      return self.cat.dequeue()
        

    if animal =='dog'  and self.dog.front:
       return self.dog.dequeue()

    if animal =='dog' or animal =='cat':
        return 'not there'     
    else :
      return 'not in the shelf for ignore it'     
