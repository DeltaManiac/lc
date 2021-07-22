# @before-stub-for-debug-begin
from python3problem236 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if root in (None, p, q): return root
            left = self.lowestCommonAncestor(root.left,p,q)
            right = self.lowestCommonAncestor(root.right,p,q)
            return root if left and right else left or right
# @lc code=end

