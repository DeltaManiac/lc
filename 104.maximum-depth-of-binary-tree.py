# @before-stub-for-debug-begin
from python3problem104 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        print (self.preorder(root,0))
        return self.preorder(root,0)

    def preorder(self,root: TreeNode,height:int) ->int:
        if not root:
            return height
        h_right = height +1
        h_left = height + 1
        if root.left != None:
            h_left = self.preorder(root.left,height+1)
        if root.right != None:
            h_right = self.preorder(root.right,height+1)
        if h_right > h_left:
            return h_right
        return h_left
# @lc code=end

