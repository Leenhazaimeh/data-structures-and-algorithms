
'''''''''
Create a Node class that has properties 
for the data stored in the node,
the left child node, and the right 
child nodes  
'''''''''


class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        
'''''''''
Create a Binary Tree class  
'''''''''
class Binary_Tree:


  def __init__(self):
        self.root = None

    

  def pre_order(self):
       
            try:
                self.nodes=[]
            
                if self.root == None:
                    return "error"

                def tree(node):
                  self.nodes+=[node.data]
                  
                  if node.right:
                        tree(node.right)
                  if node.left:
                    tree(node.left)
                  return self.nodes
                
                return tree(self.root)
            except:
                return "error"

    





  def in_order(self):
        try:

            self.nodes=[]
            
            if not self.root:
                return "error"

            def  ordered (node):
                if node.left:
                     ordered (node.left)
                self.nodes+=[node.value]
                if node.right:
                     ordered (node.right)
                return self.nodes
        
            return  ordered (self.root)
        except:
            return "error"

    
  def post_order(self):
    #  post order which returns an array of the values, ordered appropriately
        try:

            self.nodes=[]
            
            if not self.root:
                return "error"

            def  ordered (node):
                if node.right:
                    ordered (node.right)
                if node.left:
                      ordered (node.left)
                
                      self.nodes+=[node.data]
                return self.nodes
        
            return  ordered (self.root)
        except:
            return "error"



  def myMaxTree(self):
   
        if not self.root:
                return 'No tree found'
        self.myMaxTree=self.root.data


        def  ordered (node):

            if self.myMaxTree<node.data:
                self.myMaxTree=node.data


            if node.left:
                 ordered (node.left)
                 

            if node.right:
                 ordered (node.right)

            return self.myMaxTree
    
        return  ordered (self.root)


  def breadth_first(self):
        arr_nodes = [self.root]
        result = []

        if not arr_nodes[0]:
            return 'error'

        while arr_nodes:
            node=arr_nodes[0]
            if node.left:
                arr_nodes.append(node.left)
            if node.right:
                arr_nodes.append(node.right)
            result.append(arr_nodes[0].data)
            arr_nodes = arr_nodes[1:]
            
        return result



  def fizz_buzz_tree (self):
        root = self.root
        new_fbt = Binary_Tree ()

        if not root :
            return "error"

        def check_fizz_buzz(node):
            if node % 3 == 0 and node % 5 == 0:
                return ('FizzBuzz')
            elif node % 3 == 0:
                return ('Fizz')
            elif node % 5 == 0:
                return ('Buzz')
            else:
                return str(node)

        def walk(node):
            new_node = Node(check_fizz_buzz(node.data))
            if node.left:
                new_node.left = walk(node.left)
            if node.right:
                new_node.right = walk(node.right)
            return new_node

        new_fbt.root = walk(root)

        return (new_fbt)





class Binary_Search_Tree(Binary_Tree):
    '''''''''
    Create a Binary Search Tree class
This class should be a sub-class 
 of the Binary Tree Class, 
'''''''''

    def add(self,data):


        if self.root == None:
            self.root = Node(data)
        else:
            new_node =self.root
            while new_node:
                if new_node.data>data : 
                      if new_node.right == None: 
                        new_node.right = Node(data)
                        break
                        # new_node = new_node.left
                else:
                       if new_node.left == None: 
                        new_node.left = Node(data)
                        break
                        # new_node = new_node.right

 

    def Contains(self,data):
      # Returns: boolean indicating whether or not the value is in the tree at least once
        if self.root==None:
            return 'error'

        else:
            new_node=self.root
            while new_node:
                if new_node.data==data:
                    return True
                elif new_node.data > data : 
                      if new_node.right == None: 
                        return False
                        # new_node = new_node.right
                else:
                       if new_node.left == None: 
                         return False
                      #  new_node = new_node.left

if __name__ == '__main__':
   
    tree=Binary_Tree()
    tree.root=Node(3)

    tree.root.left=Node(2)
    tree.root.right=Node(13)

    tree.root.left.left=Node(4)
    tree.root.right.right=Node(7)

    tree.root.left.right=Node(5)
    tree.root.left.left.left=Node(15)

    tree.root.left.right.left=Node(4)
    tree.root.left.right.right=Node(15)


    tree.root.right.right.left=Node(18)

    
   

    new_FBTree = ((tree.fizz_buzz_tree()))
    print(new_FBTree.breadth_first())
   