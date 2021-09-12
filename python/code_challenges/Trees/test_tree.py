from tree import* 






def  test_instantiate_tree_single_root_node():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.root.data
    expected=5
    assert actual==expected



def test_add_left_fir_right_scnd():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=(tree.root.right.data,tree.root.left.data)
    expected=(3,8)
    assert actual==expected



def test_preorder_4():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.pre_order()
    expected=[5,3,8]
    assert actual==expected



def test_inorder_5():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.in_order()
    expected=[3,5,8]
    assert actual!=expected



def test_collection_from_postorder_traversal():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.post_order()
    expected=[3,8,5]
    assert actual!=expected



def test_max_val():
    tree=Binary_Search_Tree()
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

    actual=tree.myMaxTree()
    expected=18
    assert actual==expected



def test_breadth_first():
    tree = Binary_Tree()
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

    actual = tree.breadth_first()
    expected = [3, 2, 13, 4, 5, 7, 15, 4, 15, 18]

    assert actual == expected



def test_fizz_buzz_1():
    tree = Binary_Tree()

    actual = tree.fizz_buzz_tree()
    expected = "error"

    assert actual == expected

def test_empty_tree():
    test_tree=Binary_Search_Tree()
    actual=test_tree.root
    expected=None
    assert actual==expected

def test_fizz_buzz_2():
    tree = Binary_Tree()
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

    fizz_buzz = tree.fizz_buzz_tree()
    actual = fizz_buzz.breadth_first()
    expected = ['Fizz', '2', '13', '4', 'Buzz', '7', 'FizzBuzz', '4', 'FizzBuzz', 'Fizz']

    assert actual == expected