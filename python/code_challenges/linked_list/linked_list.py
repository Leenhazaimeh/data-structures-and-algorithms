class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    

    def __str__(self):
        return f"{self.data}"



class LinkedList:
  def __init__(self):
      def insert(self, data=None):

        new_node = Node(data)
       
        if self.head:
            new_node.next = self.head 
           
        self.head = new_node
    

def includes(self, value):

        current = self.head
        is_include = False
        while (current):
            if current.data == value:
                is_include = True
            current = current.next
        return is_include

def append(self, data):

        new_data = Node(data)
        current = self.head
        if self.head:
            while(current.next):
                current = current.next
            current.next = new_data
        else:
            self.head = new_data

def insertAfter(self, data, new_data):

        try:
          if self.includes(data):
              new_node = Node(new_data)
              current = self.head
              while (current):
                  if current.data == data:
                      new_node.next = current.next
                      current.next = new_node
                      break
                  current = current.next
        except:
          raise Exception("the value not found in the list")

def insertBefore(self, data, new_data):

        try:
            if self.includes(data):
                new_node = Node(new_data)
                current = self.head
                if current.data == data:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    while (current.next):
                        if current.next.data == data:
                            new_node.next = current.next
                            current.next = new_node
                            break
                        current = current.next
        except:
          raise Exception("the value not found in the list")

def kthFromEnd(self, k: int):

        length = self.length()

        if k >= length or k < 0:
            return 'IndexError'
        current = self.head
        for i in range(length-k):
            if i == length-k-1:
                return current.data
            current = current.next

def length(self):
        length = 0
        current = self.head
        while(current):
            length += 1
            current = current.next
        return length

        
def __str__(self):
 
       
        list_data = ""
      
        current = self.head
        while current:
         
            list_data += f"{current.data} -> "
           
            current = current.next
        list_data += "NULL"
       
        return list_data

        if __name__ == "__main__":
            


         linked = LinkedList()



linked.append(1)
linked.append(3)
linked.append(2)
linked.insertAfter(3, 10)
linked.insertBefore(100, 7)
linked.insertAfter(25,20)
print(linked)