# Stacks and Queues
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Challenge
Define pop, push, peak and isempty for stack and enqueue, dequeue, peak and isempty for queue.

## Approach & Efficiency
Pop O(1)
Push O(1)
Dequeue O(1) When you remove an item from a queue, you use the dequeue action. This is done with an O(1) operation in time because it doesn’t matter how many other items are in the queue, you are always just removing the front Node of the queue.

Peek O(1) : When conducting a peek, you will only be inspecting the front Node of the queue.

Typically, you want to check isEmpty before conducting a peek. This will ensure that an exception is not raised. Alternately, you can wrap the call in a try/catch block.

IsEmpty O(1) Here is the pseudocode for isEmpty

## API
[Challenge 10 - stack-and-queue](stack_and_queue.py)