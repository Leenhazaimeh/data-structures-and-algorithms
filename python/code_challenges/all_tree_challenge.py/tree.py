class tree_node : 
    def __init__(self ,value=None) :
        self.value = value  
        self.left = None
        self.right = None


        def __str__(self) :
            return str(self.value)

            class Binary_tree (tree_node):
                def __init__(self,root=None) :
                    self.root=root




                    # code challeng 15 part 1

        def pre_order(self):    
           first_list= []
        if self.root is None : 
            raise Exception("Empty Tree")
        def throgh_in(root)  : 
            first_list.append(root.value)
                
            if root.left :
                throgh_in(root.left )
            if root.right : 
                throgh_in(root.right)

        throgh_in(self.root)
        return  (first_list )
                   

        def in_order(self):  
          in_list=[] 
        if self.root is None : 
            raise Exception("empty tree")
        def throgh_in(root): 
            if root.left: 
                throgh_in(root.left)
            in_list.append (root.value)

            if root.right: 
                throgh_in(root.right)    

        throgh_in (self.root)
        return (in_list ) 

    def post_order(self, root):
        thr = []
        if root:
            thr = thr + self.post_order(root.left)
            thr = thr + self.post_order(root.right)
            thr.append(root.value)
        
        return thr

        #code challeng 16 
        def Tree_max(self): 
         max =0
        if not self.root.value : 
            return "you have an empty list "
            
        else:
            
            list = self.in_order()
            for i in list : 
                if i > max:  
                    max= i
        return max

#code challenge 17
def breadth_first(tree): 

        if tree.root is None :
            return "empty"

        else :     
            node_list=[]
            tree_list = []    

            tree_list+=[tree.root]            

       


            while tree_list : 
                our_Node =  tree_list[0]
                if our_Node.left: 
                     tree_list+=[currentNode.left]
                if our_Node.right: 
                     tree_list+=[our_Node.right]

                node_list += [ tree_list.pop(0).value]

            
        return node_list    
                    #code challeng 15 part 2
class  Binary_Search (Binary_tree) : 

    def add(self,value) : 
        if self.root: 
            def throgh_in(root):
                if value < root.value: 
                    if root.left is None :
                        root.left=tree_node(value)
                        return
                        
                    else: 
                        throgh_in(root.left)   

                elif value > root.value: 
                    if root.right is None :
                        root.right=tree_node(value)
                        return
                    else : 
                        throgh_in(root.right) 

            return throgh_in(self.root)
        else:
            self.root=tree_node(value)


    def complete(self,value):
        if not self.root:
            return False
        def throgh_in(root):
            if root:
                if root.value == value:
                    return True 
                if throgh_in(root.left):
                    return True
                if throgh_in(root.right):
                    return True
            return False
        return throgh_in(self.root)

root = tree_node(2)
root.left = tree_node(7)
root.right = tree_node(5)
root.left.left = tree_node(2)
root.left.right = tree_node(6)
root.right.right = tree_node(9)
root.left.right.left = tree_node(5)
root.left.right.right = tree_node(11)
root.right.right.left = tree_node(4)

breadthfirst(root)
