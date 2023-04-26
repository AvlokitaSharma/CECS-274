from Interfaces import Stack
import SLLStack


class MaxStack(Stack):
    def __init__(self):
        self.stack = SLLStack.SLLStack()

    def max(self) -> object:
        '''
            Returns the max element
        '''
        largest = self.stack.head.x
        h = self.stack.head
        for k in range(self.stack.n - 1):
            if largest < self.stack.head.next.x:
                largest = self.stack.head.next.x
            self.stack.head = self.stack.head.next
        self.stack.head = h
        return largest

    def push(self, x: object):
        '''
            push: Insert an element in the tail of the stack
            Inputs:
                x: Object type, i.e., any object
        '''
        return self.stack.push(x)

    def pop(self) -> object:
        '''
            pop: Remove the last element in the stack
            Returns: the object of the tail if it is no empty
        '''
        return self.stack.pop()

    def size(self) -> int:
        return self.stack.size()
# if __name__ =="__main__":
#     maxst = MaxStack()
#     maxst.push(3)
#     print(maxst.stack)
#     maxst.stack.push(1)
#     maxst.stack.push(4)
#     maxst.stack.push(2)
#     print(maxst.stack)
#     print("max_1",maxst.max())
#     print("pop_1",maxst.stack.pop())
#     print("pop_2",maxst.stack.pop())
#     print(maxst.stack)
#     print("max_2",maxst.max())
#     print("pop_3",maxst.stack.pop())
#     print("max_3",maxst.max())

