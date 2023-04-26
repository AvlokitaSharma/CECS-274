from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        super().__init__()
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x, y):
        d = BinaryTree.Node(x,y)
        d.left = d.right = d.parent = self.nil
        return d
    
        
    def find_last(self, x : object) -> BinaryTree.Node:
        k = self.r
        prev = None
        while k != None:
            prev = k
            if x < k.x:
                k = k.left
            elif k > k.x:
                k = k.right
            else:
                return k
        return prev
        
    def add_child(self, p : BinaryTree.Node, d : BinaryTree.Node) -> bool:
        if p == self.nil:
            self.r = d
        else:
            if d.x < p.x:
                p.left = d
            elif d.x > p.x:
                p.right = d
            else:
                return False
            d.parent = p
        self.n = self.n + 1
        return True

    def find_eq(self, x : object) -> object:
        k = self.r
        while k != self.nil:
            if x < k.x:
                k = k.left
            elif x > k.x:
                k = k.right
            else:
                return k
        return self.nil
    
    def find(self, x: object) -> object:
        k = self.r
        z = self.nil
        while k != self.nil:
            if x < k.x:
                z = k
                k = k.left
            elif x > k.x:
                k = k.right
            else:
                return k
        if z == self.nil:
            return self.nil
        return z.v

        
    def add(self, key : object, value : object) -> bool:
        p = self.find_last(key)
        a = self.add_child(p, self.new_node(key, value))
        return a

    def add_node(self, k : BinaryTree.Node) -> bool:
        pass
    
    def splice(self, k: BinaryTree.Node):
        if k.left != self.nil:
            s = k.left
        else:
            s = k.right
        if k == self.r:
            self.r = s
            p = self.nil
        else:
            p = k.parent
            if p.left == k:
                p.left = s
            else:
                p.right = s
        if s != self.nil:
            s.parent = p
        self.n -= 1

    def remove_node(self, k : BinaryTree.Node):
        if k.left == self.nil or k.right == self.nil:
            self.splice(k)
        else:
            w = k.right
            while w.left != self.nil:
                w = w.left
            k.x = w.x
            k.v = w.v
            self.splice(w)

    def remove(self, x : object) -> bool:
        k = self.find_eq(x)
        if k != self.nil:
            self.remove_node(k)
            return True
        return False

             
    def __iter__(self):
        k = self.first_node()
        while k != self.nil:
            yield k.x
            k = self.next_node(k)

if __name__ == "__main__":
    q = BinarySearchTree()
    q.add(1, "First")
    q.add(2, "Second")
    q.add(3, "Third")
    print(q.find(2.5))
    print(q.find_eq(3))
    
    
'''         
q = BinarySearchTree()
q.add(3, "third")
q.add(2, "second")
q.add(1, "first")
print(q.find(2.5))
q.remove(3)
print(q.find(3))
q.add(3, "third")
q.add(5, "fifth")
q.add(4, "fourth")
print(q.find_eq(3.4))
print(q.find(3.4))
print("In order")
q.in_order()
print("Pre oder")
q.pre_order()
print("Pos order")
q.pos_order()
'''