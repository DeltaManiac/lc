# @before-stub-for-debug-begin
from python3problem122 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                max_profit += prices[i]-prices[i-1]
        return max_profit

# @lc code=end

