from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
   
    def push(self, x : np.object) :
        a = self.Node(x)
        a.next = self.head
        self.head = a
        self.n = self.n + 1
        if self.n == 1:
            self.tail = self.head
        
    def pop(self) -> np.object:
        try:
            if self.n == 0:
                raise Exception
            x = self.head.x
            self.head = self.head.next
            self.n = self.n - 1
            if self.n == 0:
                self.tail = None
            return x
        except Exception:
            print("Linekd List Stack is Already Empty!")
            
    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
        
'''
if __name__ == "__main__":
    sll = SLLStack()
    print(sll.pop())
    sll.push(1)
    sll.push(2)
    sll.push(3)
    sll.push(4)
    sll.push(5)
    print(sll.pop())
    print(sll.pop())
    print(sll.pop())
    print(sll.pop())
    print(sll.pop())
'''
