from new_qeue import *

class Node():
 def __init__(self,value=None) -> None:
       
        self.value=value
        self.next=None



class Stack():
    def __init__(self,node=None) -> None:
        self.top=node

    def push(self,value=None):
        try:
            node=Node(value)
            node.next=self.top
            self.top=node
        except:
            raise Exception('Flaaase ')

    def peek(self):
       
        try:
         return self.top.value
        except:
         raise Exception('empty Stake')
    def pop(self):
        try:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value
        except:
            raise Exception(' empty Stake ')
    
    def is_empty(self):
    
        return not self.top

 


class Queue():
    def __init__(self) :

       self.rear=None
       self.front=None
        
    
    def enqueue(self,value):
      
        node=Node(value)
        if not self.front and not self.rear:
            self.front=node
            self.rear=node

        else:    
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        
        try:
            temp=self.front
            self.front=self.front.next
            temp.next=None

            if self.front==None:
                 self.rear=None

            return temp.value
        except:
            raise Exception("  empty Queue")

    def peek(self):
       
        try:
         return self.front.value
        except:
         raise Exception("empty Queue")

    def is_empty(self):
        
      return not self.top
    
    def __str__(self):
        string=""
        while self.front:
            string+=f"{self.front.value}  "
            self.front=self.front.next
        string+="None" 
        return(string)

    
class Animal_Shelter():
    def __init__(self) :
      self.cats=Queue()
      self.dogs=Queue()
        

    def dequeue(self,pref):

        if pref=="Dog" or pref=="dog" :
           return self.dogs.dequeue()

        elif pref=="Cat" or pref=="cat":
           return self.cats.dequeue()

        else:
            return None
   
    def enqueue(self,animal):

        if animal.type=="Cat":
            self.cats.enqueue(animal)
        elif  animal.type=="Dog":
            self.dogs.enqueue(animal)
    
    

            
            
class Cat():
    def __init__(self,name) :
        self.type="Cat"
        self.name=name

class Dog():
    def __init__(self,name) :
        self.type="Dog"
        self.name=name





# if __name__=="__main__":

#  print ('Hello leen')

