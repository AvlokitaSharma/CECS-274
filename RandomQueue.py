import random
from Interfaces import Queue
import ArrayQueue


class RandomQueue(Queue):
    def __init__(self):
        self.queue = ArrayQueue.ArrayQueue()


    def add(self, x : object) -> object:
        return self.queue.add(x)



    def remove(self) -> object:
        '''
            remove: remove the next (previously added) value, y, from the
                    Queue and return y. The Queue’s queueing discipline
                    decides which element should be removed.
            Return: Object type
        '''
        if self.queue.n == 0:
            raise IndexError()
        x = random.randint(0, self.queue.n)
        b = self.queue.new_array(len(self.queue.a))
        for i in range(0,x):
            b[i] = self.queue.a[i]
        for i in range(x+1,self.queue.n+1):
            b[i] = self.queue.a[i]
        self.queue.a = b
        self.queue.n -= 1
        if x == 0:
            self.queue.j = (self.queue.j+1) % len(self.queue.a)
        if len(self.queue.a) >= 3*self.queue.n:
            self.queue.a.resize()
        return x


    def size(self) -> int:
        return self.queue.size()

# if __name__ == "__main__":
#     rq = RandomQueue()
#     rq.add(0)
#     rq.add(1)
#     rq.add(2)
#     rq.add(3)
#     rq.add(4)
#     print(rq.queue.a)
#     rq.remove()
#     rq.remove()
#     rq.remove()
#     rq.remove()
#     rq.remove()
#     print(rq.queue.a)



