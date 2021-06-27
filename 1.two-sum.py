#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap={}
        for i,n in enumerate(nums):
            m = target - n
            if m in numMap:
                return [numMap[m],i]
            else:
                numMap[n] = i
# @lc code=end

