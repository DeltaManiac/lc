# @before-stub-for-debug-begin
from python3problem112 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root: TreeNode) -> bool:
        return root.left is None and root.right is None

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum==0
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right, targetSum)
# @lc code=end

