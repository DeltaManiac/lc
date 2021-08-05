# @before-stub-for-debug-begin
from python3problem62 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(2)]

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[0][c] = dp[1][c] + dp[0][c+1]
            dp[1] = dp[0]

        return dp[0][0]
# @lc code=end

