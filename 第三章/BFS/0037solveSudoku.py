#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 10971892875@qq.com
#    > Created Time: 2020年4月2日
#    > description: 
#######################################################################
'''
(37. 解数独)[https://leetcode-cn.com/problems/sudoku-solver/
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。
'''
import unittest
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)
        return board
    def backtrack(self, board, row, col):
        m, n = 9, 9
        if row == m:
            return True
        if col == n:
            return self.backtrack(board, row + 1, 0)
        
        if board[row][col] != '.':
            return self.backtrack(board, row, col + 1)
        for c in range(9):
            ch = chr(c+49)
            if not self.isvalid(board, row, col, ch):
                continue
            board[row][col] = ch
            if self.backtrack(board, row, col + 1):
                return True
            board[row][col] = '.'
        return False
    def isvalid(self, board, row, col, ch):

        for i in range(9):
            if board[row][i] == ch:
                return False
            if board[i][col] == ch:
                return False
            if board[3*(row//3) + i//3][3*(col//3)+i%3] == ch:
                return False

        return True
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

        res = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

        self.assertEqual(res, Solution().solveSudoku(board))

if __name__ == "__main__":
    unittest.main()

