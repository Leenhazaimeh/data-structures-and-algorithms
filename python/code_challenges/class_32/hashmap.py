

def tree_intersection(binary_trees1,binary_trees2):
    if (binary_trees1.root and binary_trees2.root):
        binary_trees1_list=binary_trees1.in_order()
        binary_trees2_list=binary_trees2.in_order()
        binary_trees=[]
        for j in binary_trees1_list:
            if j in binary_trees2_list:
                binary_trees.append(j)
        return binary_trees
    else:
         return 'you have an  empty tree'


binary_trees1=[150,200.100]
binary_trees2=[99,89,97]
print (tree_intersection(binary_trees1,binary_trees2))  