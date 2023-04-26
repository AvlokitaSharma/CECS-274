from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: np.object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i > self.n:
            raise Exception()
        if i < self.n / 2:
            p = self.dummy.next
            for x in range(i):
                p = p.next
        else:
            p = self.dummy
            for x in range(self.n - i):
                p = p.prev
        return p

    def get(self, i) -> np.object:
        p = self.get_node(i)
        return p.x

    def set(self, i: int, x: np.object) -> np.object:
        p = self.get_node(i)
        y = p.x
        p.x = x
        return y

    def add_before(self, w: Node, x: np.object) -> Node:
        if w is None:
            raise Exception()
        u = self.Node(x)
        u.next = w
        u.prev = w.prev
        u.next.prev = u
        u.prev.next = u
        self.n += 1

    def add(self, i: int, x: np.object):
        self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        pass

    def remove(self, i: int):
        if self.n == 0:
            raise IndexError()
        w = self.get_node(i)
        w.next.prev = w.prev
        w.prev.next = w.next
        self.n -= 1
        return w.x

    def size(self) -> int:
        return self.n

    def append(self, x: np.object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        for x in range(self.n - 1):
            if self.get(x) != self.get((self.n-1)-x):
                return False
        return True




    def reverse(self):
        for x in range(0, self.n - 1):
            self.add(x, self.get(self.n - 1))
            self.dummy.prev = self.dummy.prev.prev
            self.dummy.prev.next = self.dummy
            self.n -= 1






    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __getitem__(self, i) -> object:
        '''
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input:
                i: positive integer less than n
            Return: the item at index i
        '''
        if isinstance(i, slice):
            raise "Not implemented. Please use the references next and prev"
        else:
            return self.get(i)

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
if __name__ == "__main__":
    dll = DLList()
    dll.add(0,"a")
    dll.add(1,"b")
    dll.add(2, "c")
    dll.add(3,"d")
    dll.add(4, "e")
    print(dll)
    dll.reverse()
    print(dll)





