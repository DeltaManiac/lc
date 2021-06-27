# @before-stub-for-debug-begin
from python3problem123 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = two_buy =   sys.maxsize
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy,p)
            one_profit = max(one_profit,p - one_buy)
            two_buy = min(two_buy,p - one_profit)
            two_profit = max(two_profit,p - two_buy)
        return two_profit
# @lc code=end

