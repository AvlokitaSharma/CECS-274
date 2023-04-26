import ArrayQueue
#from drawtree import draw_bst

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x) :
            self.x = x

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u : Node) -> int:
        if u == self.nil:
            return -1
        D = 0
        while u != self.r:
            u = u.parent
            D = D + 1
        return D


    def size(self) -> int:
        return self._size(self.r)

    
    def _size(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + self._size(u.left) + self._size(u.right)
    
    def size2(self) -> int:
        u = self.r
        p_r_v = self.nil
        N = 0
        while u != self.nil:
            if p_r_v == u.parent:
                N += 1
                if u.left != self.nil:
                    n_x_t = u.left
                elif u.right != self.nil:
                    n_x_t = u.right
                else:
                    n_x_t = u.parent
            elif p_r_v == u.left:
                if u.right != self.nil:
                    n_x_t = u.right
                else:
                    n_x_t = u.parent
            else:
                n_x_t = u.parent
            p_r_v = u
            u = n_x_t
        return N

    def height(self) -> int:
        return self._height(self.r)
    
    def _height(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + max(self._height(u.left), self._height(u.right))
    
    def traverse(self, u : Node):
        pass

    def traverse2(self):
        u = self.r
        p_r_v = self.nil
        while u != self.nil:
            if p_r_v == u.parent:
                if u.left != self.nil:
                    n_x_t = u.left
                if u.right != self.nil:
                    n_x_t = u.right
                if u.left == self.nil and u.right == self.nil:
                    n_x_t = u.parent
            elif p_r_v == u.left:
                if u.right != self.nil:
                    n_x_t = u.right
                else:
                    n_x_t = u.parent
            else p_r_v == u.right:
                n_x_t = u.parent
            p_r_v = u
            p_r_v = u
            u = n_x_t


    def bf_traverse(self):
        k = ArrayQueue.ArrayQueue()
        k.add(self.r)
        while k.size() > 0:
            u = k.remove()
            if u.left != self.nil:
                k.add(u.left)
            if u.right != self.nil:
                k.add(u.right)

    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
    
    def in_order(self) :       
        if self.r is not self.nil:
            self.__in_order(self.r)

    def pre_order(self) :       
        if self.r is not self.nil:
            self.__pre_order(self.r)

    def pos_order(self) :       
        if self.r is not self.nil:
            self.__pos_order(self.r)

    def __in_order(self, u : Node) : 
        if u.right is not self.nil:
            self.__in_order(u.right)    
        if u.left is not self.nil:
            self.__in_order(u.left)
        print(f"{u.x}: {u.v}")     
        

    def __pre_order(self, u : Node) :  
        print(f"{u.x}: {u.v}")
        if u.right is not self.nil:
            self.__pre_order(u.right)
        if u.left is not self.nil:
            self.__pre_order(u.left)
        

    def __pos_order(self, u : Node) :  
        if u.right is not self.nil:
            self.__pos_order(u.right)
        if u.left is not self.nil:
            self.__pos_order(u.left)
       
        print(f"{u.x}: {u.v}")     

    def __str__(self):
        l = []
        #self.in_order(self.r, l)
        return ', '.join(map(str, l))