#
# @lc app=leetcode id=1628 lang=python3
#
# [1628] Design an Expression Tree With Evaluate Function
#

# @lc code=start
import abc
from abc import ABC, abstractmethod
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class BinaryNode(Node):
    def __init__(self, _left, _right):
        self.left = _left
        self.right = _right
    def evaluate(self) -> int:
        pass

class Add(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()

class Subtract(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate()- self.right.evaluate()

class Divide(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()

class Multiply(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() //  self.right.evaluate()

class Number(Node):
    def __init__(self,_val) -> None:
        self.value = _val
    def evaluate(self) -> int:
        return self.value
"""
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        ops = {'+':Add,'-':Subtract,'*':Multiply,'/':Divide}
        stk=[]
        for token in postfix:
            if token in ops:
                R = stk.pop()
                L = stk.pop()
                stk.append(ops[token](L,R))
            else:
                stk.append(Number(int(token)))
        return stk[0]

# @lc code=end

