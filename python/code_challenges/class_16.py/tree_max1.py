class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

''''''
# Find the Maximum Value in a Binary Tree
''''''
def MaxValue(root):

    def inorder(tree):
        if tree:
            inorder(tree.left)
            if not (tree.val in uniques):
                uniques.add(tree.val)
            inorder(tree.right)

    uniques = set()
    inorder(root)
    arr = list(uniques)
# now the nodes order from the max value to min value
    cont = 1

    if len(arr) > cont:
        return arr[len(arr) - cont]
    else:
        return -1


if __name__ == "__main__":

    tree1 = TreeNode(3)

    tree1.left = TreeNode(2)
    tree1.right = TreeNode(5)

    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(3)

    tree1.right.left = TreeNode(5)
    tree1.right.right = TreeNode(7)

    print(MaxValue(tree1))