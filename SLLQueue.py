from Interfaces import Queue
import numpy as np

class SLLQueue(Queue):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
        

    def add(self, x :np.object) :
        a = self.Node(x)
        if self.n == 0:
            self.head = a
        else:
            self.tail.next = a
        self.tail = a
        self.n = self.n + 1

    def remove(self) -> np.object:
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
            print("Linekd List Queue is Already Empty!")

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
    sll = SLLQueue()
    sll.remove()
    sll.add(1)
    sll.add(2)
    sll.add(3)
    sll.add(4)
    sll.add(5)
    print(sll)
    print(sll.remove())
    print(sll.remove())
    print(sll.remove())
    print(sll.remove())
    print(sll.remove())
'''
    