# @before-stub-for-debug-begin
from python3problem212 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        trie={}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter,{})
            node[WORD_KEY] =word
        rowNum = len(board)
        colNum = len(board[0])
        sol = []
        def bk(row,col,parent):
            letter = board[row][col]
            currNode = parent[letter]
            word_match= currNode.pop(WORD_KEY,False)
            if word_match:
                sol.append(word_match)
            board[row][col] = '#'
            for (rowOffset, colOffset) in [(-1,0),(0,1),(1,0),(0,-1)]:
                newRow, newCol = row + rowOffset, col+colOffset
                if newRow<0 or newRow>= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                bk(newRow,newCol,currNode)
            board[row][col]= letter

            if not currNode:
                parent.pop(letter)
        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col]in trie:
                    bk( row,col,trie)
        return sol
# @lc code=end

