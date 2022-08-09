##############################################
# Title: Queue Analysis
# Author: Rhea Toves
# Version: 1.0
# Date: March 22, 2022
#
# Description: This program creates stacks and queues.
# This also works with 1000, 10000, and 100000 data
# points - while recording the performance times
# for some methods.
###############################################
import time

def create_stack():
    # Creates a stack
    return []

class Stack:
    items = []

    def __init__(self):
        # Creates a new stack that is empty. It needs no parameters and returns an empty stack.
        self.items = []

    def __str__(self):
        temp_str = "Bottom: "
        for item in self.items:
            temp_str += str(item) + " "
        return temp_str + ":Top"

    def is_empty(self):
        # Tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
        return self.items == []

    def push(self, item):
        # Adds a new item to the top of the stack. It needs the item and returns nothing.
        self.items.append(item)

    def pop(self):
        # Removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
        if len(self.items) != 0:
            x = self.items[len(self.items) - 1]
            self.items.pop()
            return x
        else:
            return None

    def peek(self):
        # Returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
        return self.items[len(self.items) - 1]

    def size(self):
        # Returns the number of items on the stack. It needs no parameters and returns an integer.
        return len(self.items)

def create_queue():
    # Create a queue
    return Queue()

class Queue:
    def __init__(self):
        # Creates a new queue that is empty. It needs no parameters and returns an empty queue.
        self.stack1 = []
        self.stack2 = []

    def __str__(self):
        temp_str = "Front: "
        for item in self.stack1:
            temp_str += str(item) + " "
        return temp_str + ":Rear"

    def is_empty(self):
        # Tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
        return self.stack1 == []

    def enqueue(self, items):
        # Adds a new item to the rear of the queue. It needs the item and returns nothing.
        self.stack1.append(items)

    def dequeue(self):
        # Removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
        if len(self.stack1) == 0:
            print("Queue is empty!")
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        i = self.stack2[-1]
        self.stack2.pop()

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
        return i

    def size(self):
        # Returns the number of items in the queue. It needs no parameters and returns an integer.
        return len(self.items)

class Dequeue:
    def __init__(self):
        # Creates a new deque that is empty. It needs no parameters and returns an empty deque.
        self.stack1 = []
        self.stack2 = []

    def __str__(self):
        temp_str = "Front: "
        for item in self.stack1:
            temp_str += str(item) + " "
        return temp_str + ":Rear"

    def is_empty(self):
        # Tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
        return self.stack1 == []

    def add_front(self, item):
        # Adds a new item to the front of the deque. It needs the item and returns nothing.
        while True:
            i = self.stack1.pop(0)
            if i is not None:
                self.stack2.insert(i)
            else:
                break
            self.stack2.insert(item)

        while True:
            i = self.stack2.pop(0)
            if i is not None:
                self.stack1.insert(i)
            else:
                break
            self.stack1.insert(item)

    def add_rear(self, item):
        # Adds a new item to the rear of the deque. It needs the item and returns nothing.
        while True:
            i = self.stack1.pop()
            if i is not None:
                self.stack2.append(i)
            else:
                break
            self.stack2.append(item)

        while True:
            i = self.stack2.pop()
            if i is not None:
                self.stack1.append(i)
            else:
                break
            self.stack1.append(item)

    def remove_front(self):
        # Removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
        if self.stack1 is not None:
            self.stack1.pop(0)
        if self.stack2 is not None:
            self.stack2.pop(0)

    def remove_rear(self):
        # Removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
        if self.stack1 is not None:
            self.stack1.pop(0)
        if self.stack2 is not None:
            self.stack2.pop(0)

    def size(self):
        # Returns the number of items in the deque. It needs no parameters and returns an integer.
        return len(self.items)

def main():

    with open(file="words.txt") as file:
        for n in [int(1000), int(10000), int(100000)]:
            lines = [next(file) for x in range(n)]
            start_time = time.time()
            q = create_queue()
            q.enqueue(lines)
            end_time = time.time()
            print(q)
            print("Enqueue Time: ", start_time - end_time)
            start_time = time.time()
            d = Dequeue()
            print(d)
            end_time = time.time()
            print("Dequeue Time: ", start_time - end_time)
            print()

main()

'''
Conceptual Questions:
1) I used "Q = create_queue()", "enqueue(i)", and "i = dequeue()" in my main function.
2) The worst case running time for my dequeue implementation is when stack1 is filling up with n elements but
we want to perform Dequeue() on stack1 and this would take O(n) time.
3) Over a series of n enqueues, the pop() operation is not used. Over a series of n dequeues, the pop() operation
is used x amount of times plus the n number of elements in stack1.
'''