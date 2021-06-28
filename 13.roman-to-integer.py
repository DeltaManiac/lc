# @before-stub-for-debug-begin
from python3problem13 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
#
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        _dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        sum = 0
        for i in s[::-1]:
            curr = _dict[i]
            if prev > curr:
                sum -= curr
            else:
                sum += curr
            prev = curr
        return sum
# @lc code=end

