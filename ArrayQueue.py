import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
        
    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)
    
    def resize(self):
        temp_stack = self.new_array(max(1, 2 * self.n))
        for i in range(0, self.n):
            temp_stack[i] = self.a[(self.j + i) % len(self.a)]
        self.a = temp_stack
        self.j = 0

    def add(self, x : np.object) :
        temp = self.n
        if (self.n + 1) > len(self.a):
            self.resize()
            self.n = temp
        self.a[(self.j + self.n) % len(self.a)] = x
        self.n = self.n + 1
        return True

    def remove(self) -> np.object :
        try:
            if self.n == 0:
                raise Exception
            else:
                x = self.a[self.j]
                self.j = (self.j + 1) % len(self.a)
                self.n -= 1
                if len(self.a) >= 3 * self.n:
                    self.resize()
                return x
        except Exception:
            print("Queue is empty!")

    def size(self) :
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x
'''
if __name__ == "__main__":
    x = ArrayQueue()
    x.remove()
    x.add(1)
    print(x)
    x.add(2)
    print(x)
    x.add(3)
    print(x)
    x.add(4)
    print(x)
    x.add(5)
    print(x)
    
    x.remove()
    print(x)
    x.remove()
    print(x)
    x.remove()
    print(x)
    x.remove()
    print(x)
    x.remove()
    print(x)
'''