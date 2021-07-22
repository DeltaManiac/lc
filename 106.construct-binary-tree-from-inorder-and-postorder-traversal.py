# @before-stub-for-debug-begin
from python3problem106 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left,in_right):
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]
            root.right = helper(index +1, in_right)
            root.left = helper(in_left, index-1)
            return root

        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0,len(inorder) - 1)

# @lc code=end

