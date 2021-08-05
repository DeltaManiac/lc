# @before-stub-for-debug-begin
from python3problem17 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    Letter = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
    def letterCombinations(self, digits: str) -> List[str]:
        digit_count = len(digits)
        sol = []
        if digits=="":
            return []
        def DFS(pos:int,st:str):
            if pos==digit_count:
                sol.append(st)
            else:
                chars = self.Letter[digits[pos]]
                for ch in chars:
                    DFS(pos+1,st+ch)
        DFS(0,"")
        return sol
# @lc code=end

