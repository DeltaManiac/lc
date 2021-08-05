# @before-stub-for-debug-begin
from python3problem133 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_map= {}
        node_visited_map= {}
        queue = [node]
        while queue:
            ptr = queue.pop(0)
            if ptr.val not in node_visited_map.keys():
                if ptr.val not in node_map:
                    node_map[ptr.val] = Node(ptr.val,None)
                if ptr.val not in node_visited_map:
                    node_visited_map[ptr.val] = ptr
                for c in ptr.neighbors  :
                        queue.append(c)
        for ptr in node_visited_map.values():
            curr = node_map[ptr.val]
            curr.neighbors = []
            for child in ptr.neighbors:
                curr.neighbors.append(node_map[child.val])


        return node_map.get(node.val)
# @lc code=end

