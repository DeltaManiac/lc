# @before-stub-for-debug-begin
from python3problem7 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1
            x = x*neg
        rev = x%10
        x = x//10
        while x>0:
            rev =  rev*10
            rev += x%10
            x = x//10
        if rev * neg > pow(2,31) - 1 or rev *neg < -pow(2,31):
            return 0
        return rev *neg
# @lc code=end

