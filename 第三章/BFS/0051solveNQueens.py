#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################

import unittest
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [["." for _ in range(n)] for _ in range(n) ]
        self.res = []
        self.backtrack(board, 0)
        return self.res
    def backtrack(self, board, row):
        if row == len(board):
            self.res.append(["".join(board[i]) for i in range(len(board))])
            return 
        for col in range(len(board[row])):
            if not self.isvalid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'

    def isvalid(self, board, row, col):
        n = len(board)
        # 只比较上半部分即可
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        for i,j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 'Q':
                return False

        for i,j in zip(range(row-1, -1, -1),range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 4
        res = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        self.assertEqual(res, Solution().solveNQueens(s))

if __name__ == "__main__":
    unittest.main()
  
