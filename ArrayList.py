import numpy as np
from Interfaces import List

class ArrayList(List):

    def __init__(self):

        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
        
    def new_array(self, n : int) ->np.array:  
        return np.zeros(n, np.object)
    
    def resize(self):
        temp_list = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            temp_list[i] = self.a[(self.j + i) % len(self.a)]
        self.a = temp_list
        self.j = 0

    def get(self, i : int) -> object:
        try:
            if i < 0 or i > self.n - 1:
                raise Exception
            else:
                return self.a[(self.j + i) % len(self.a)]
        except:
            raise IndexError()

    def set(self, i : int, x : object) -> object:
        try:
            if i < 0 or i > self.n - 1:
                raise Exception
            else:
                y = self.a[(self.j + i) % len(self.a)]
                self.a[(self.j + i) % len(self.a)] = x
                return y
        except Exception:
            raise IndexError()
            

    def append(self, x : object) :  
        self.add(self.n, x)
        
    def add(self, i : int, x : object) :
        try:
            if i < 0 or i > self.n:
                raise Exception
            if self.n == len(self.a):
                self.resize()
            if i < self.n/2:
                self.j = (self.j - 1) % len(self.a)
                for k in range(0, i):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
            else:
                for k in range(self.n, i, -1):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
            self.a[(self.j + i) % len(self.a)] = x
            self.n =  self.n + 1
        except Exception:
            raise IndexError()
    
    def remove(self, i : int) -> object:
        try:
            if i < 0 or i >= self.n:
                raise Exception
            x = self.a[(self.j + i) % len(self.a)]
            if i < self.n/2:
                for k in range(i, 0, -1):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
                self.j = (self.j + 1) % len(self.a)
            else:
                for k in range(i, self.n - 1):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
            self.n -= 1
            if len(self.a) >= 3 * self.n:
                self.resize()
            return x
        except Exception:
            raise IndexError()

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        s += f"] {self.n} : {self.j}"
        return s

    def __getitem__(self, i) -> object:
        if isinstance(i, slice):
            return [self.get(i) for i in range(i.start, i.stop)]
        else:
            return self.get(i)

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator +=1
        else:
             raise StopIteration()
        return x


'''
if __name__ == "__main__":
    arraylist = ArrayList()
    arraylist.add(0,4)
    arraylist.add(0,1)
    arraylist.add(1,3)
    arraylist.add(1,2)
    arraylist.add(4,5)
    print(arraylist)
    print(arraylist.get(0))
    arraylist.remove(2)
    print(arraylist)
    arraylist.remove(3)
    print(arraylist)
'''