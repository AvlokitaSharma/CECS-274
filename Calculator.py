import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, m: str, v: float):
        self.dict.add(m, v)

    def print_expression(self, s: str) -> str:
        q = ''
        for item in s:
            val = self.dict.find(item)
            if val != None:
                q += str(val)
            else:
                q += item
        return q

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for x in s:
            if x == "(":
                stack.push(x)
            elif x == ")":
                if stack.size() == 0:
                    return False
                else:
                    stack.pop()
        if stack.size() == 0:
            return True
        else:
            return False

    def build_parse_tree(self, exp: str) -> str:
        q = BinaryTree.BinaryTree()
        q.r = q.Node(' ')
        y = q.r
        for i in exp:
            if i == "(":
                y = y.insert_left()
            elif i == "a" or i == "b" or i == "c" or i == "d":
                y.x = i
                y = y.parent
            elif i == "+" or i == "-" or i == "*" or i == "/":
                y.x = i
                y = y.insert_right()
            elif i == ")":
                y = y.parent
        return t

    def _evaluate(self, u):
        opr = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/' :operator.truediv}
        if u.left != None and u.right != None:
            f_n = opr[u.x]
            return f_n(self._evaluate(u.left),self._evaluate(u.right))
        elif u.left == None and u.right == None:
            t = self.dict.find(u.x)
            if t != None:
                return t
            return u.x
        else:
            if u.left != None:
                return self._evaluate(u.left)
            else:
                return self._evaluate(u.right)
        return 0


    def evaluate(self, exp):
        try:
            parseTree = self.build_parse_tree(exp)
            return self._evaluate(parseTree.r)

        except:
            return 0


'''
s = Calculator()
print(s.evaluate("((a*b)+(c*d))"))
s.set_variable("a", 1.3)
s.set_variable("b", 2.1)
s.set_variable("c", 2.2)
s.set_variable("d", 3.0)
print(s.evaluate("((a*b)+(c*d))"))
'''


