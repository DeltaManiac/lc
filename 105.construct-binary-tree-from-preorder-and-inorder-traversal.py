# @before-stub-for-debug-begin
from python3problem105 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left,in_right):
            nonlocal preoder_index
            if in_left>in_right:
               return None
            val = preorder[preoder_index]
            root = TreeNode(val)
            preoder_index +=1
            root.left = helper(in_left, idx_map[val]-1)
            root.right = helper(idx_map[val]+1, in_right)
            return root

        preoder_index= 0
        idx_map={val:idx for idx,val in enumerate(inorder)}
        a = helper(0,len(preorder)-1)
        return a
# @lc code=end

