https://miro.com/app/board/o9J_ly20lm4=/ 
# Challenge Summary
## Features
Node

    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Binary Tree

    Create a Binary Tree class
        Define a method for each of the depth first traversals:
            * pre order
            * in order
            * post order which returns an array of the values, ordered * appropriately.
        Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

Binary Search Tree

    Create a Binary Search Tree class
        This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
        Add
            Arguments: value
            Return: nothing
            Adds a new node with that value in the correct location in the binary search tree.
    Contains
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.


## Whiteboard Process
![Challenge  - all_trees](Capturenew2.PNG)

## Approach & Efficiency

    pre order: time O(n), space O(n)
    in order: time O(n), space O(n)
    post order: time O(n), space O(n)
    Add: time O(logn), space O(1)
    Contains: time O(logn), space O(1)


## Solution
[Challenge  - all_trees](./Trees/tree.py)

# Challenge Summary Code Challenge: Class 16 : Find the Maximum Value in a Binary Tree

    find maximum value
        Arguments: none
        Returns: number

Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process
![Challenge 113 - all_trees](assist/Untitled(1).jpg)

## Approach & Efficiency
max: time O(n), space O(1)

## Solution
[Challenge  - all_trees](./Trees/tree.py)


# Challenge Summary  Code Challenge: Class 17 : Breadth-first Traversal.
Feature Tasks

    Write a function called breadth first
    Arguments: tree
    Return: list of all values in the tree, in the order they were encountered

NOTE: Traverse the input tree using a Breadth-first approach

## Whiteboard Process
![Challenge 113 - all_trees](assist/Untitled(3).jpg)

## Approach & Efficiency

    Time : O(n)
    Space: O(n)
## Solution
[Challenge  - all_trees](./Trees/tree.py)

# Challenge Summary Code Challenge: Class 18 : Fizz Buzz Tree
Feature Tasks

    Write a function called fizz buzz tree
    Arguments: k-ary tree
    Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

    1. If the value is divisible by 3, replace the value with “Fizz”
    2. If the value is divisible by 5, replace the value with “Buzz”
    3. If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    4. If the value is not divisible by 3 or 5, simply turn the number into a String.


## Whiteboard Process
![Challenge 113 - all_trees](assist/Untitled(4).jpg)

# the miro link : https://miro.com/app/board/o9J_ly20lm4=/ 

## Approach & Efficiency

    Time : O(n)
    Space: O(n)


## Solution
[Challenge  - all_trees](./Trees/tree.py)

