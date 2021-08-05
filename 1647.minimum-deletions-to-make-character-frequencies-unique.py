#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str) -> int:
       char_map = {}
       for c in s:
           char_map[c] = char_map.get(c,0)+1
       values = list(char_map.values())
       values.sort()
       count = 0
       for x in range(len(values)-1):
          if values[x] == values[x+1]:
              values[x+1] = values[x+1] -1
              count+=1
       return 0
# @lc code=end