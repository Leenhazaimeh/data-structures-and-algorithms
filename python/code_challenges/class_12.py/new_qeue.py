class Node:
  def __init__(self , value=None):
    self.value= value
    self.next=None




class StackEmptyException(Exception):
   pass

class Stack:
    def __init__(self,node=None):
        self.top=node
  
    def push(self, value):
        node= Node(value) 
        node.next = self.top 
        self.top = node

    def pop(self):
        temp=self.top
        self.top=self.top.next
        temp.next=None
        return temp.value

    def peek(self):
        if not self.top:
            raise Exception('empty stack')
        else:
            return self.top.value
    

    def is_empty(self):
        return not self.top    
