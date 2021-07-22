#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        a = []
        root.next=None
        b = []
        if  root.left is not None: b.append(root.left)
        if  root.right is not None: b.append(root.right)
        a.append(b)
        while len(a)>0:
            b = a.pop(0)
            c = []
            for idx,node in enumerate(b):
                if  node.left is not None: c.append(node.left)
                if  node.right is not None: c.append(node.right)
                if idx<len(b)-1:
                    node.next=b[idx+1]
            if len(c)>0:
                a.append(c)
        return root
# @lc code=end

