class Node:
  ''''
 my counstructur __init__
  '''
  def __init__(self, value):
    self.value = value
    self.next = None

  def add(self, data):
    return Node(self.value + data.value)

  def __str__(self):
    return str(self.value)


class LinkedList():

  '''
 creat the list 
  '''
  def __init__(self):
    self.head = None
  '''
 include method 
  '''
  def includes(self,vlaue):
     current=self.head
     while current :
        
         if vlaue ==current.value[0]:
            return True
         current=current.next
     return False
     
  def insert(self, value):
    node = Node(value)

    if self.head:
      node.next = self.head

    self.head = node

  '''
 append method 
  '''
  def append(self,value):
    new_node=Node(value)

    if self.head == None:
      self.head = new_node
    else:
      current=self.head
      while current.next:
        current=current.next
      current.next=new_node

      