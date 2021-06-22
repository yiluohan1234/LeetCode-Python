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
class UF(object):
    def __init__(self, n):
        self.count = n
        self.parent = [ i for i in range(n)]
        self.size = [1 for i in range(n)]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = self.parent[rootP]
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = self.parent[rootQ]
            self.size[rootQ] += self.size[rootP]
        self.count -= 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        return rootP == rootQ

    def getCount(self):
        return self.count
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: 
            return

        m = len(board)
        n = len(board[0])
        #给 dummy 留一个额外位置
        uf = UF(m * n + 1)
        dummy = m * n
        # 将首列和末列的 O 与 dummy 连通
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(i * n, dummy)
            if board[i][n - 1] == 'O':
                uf.union(i * n + n - 1, dummy)
        
        # 将首行和末行的 O 与 dummy 连通
        for j in range(n):
            if board[0][j] == 'O':
                uf.union(j, dummy)
            if board[m - 1][j] == 'O':
                uf.union(n * (m - 1) + j, dummy)
        
        #方向数组 d 是上下左右搜索的常用手法
        dev = [(1,0), (0,1), (0,-1), (-1,0)]
        for i in range(1, m-1): 
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    # 将此 O 与上下左右的 O 连通
                    for dx,dy in dev:
                        x = i + dx
                        y = j + dy
                        if board[x][y] == 'O':
                            uf.union(x * n + y, i * n + j)
                    
        # 所有不和 dummy 连通的 O，都要被替换
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not uf.connected(dummy, i * n + j):
                    board[i][j] = 'X'
        return board
class TestSolution(unittest.TestCase):
    
    def test_0(self):
        s = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
        res = [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
        self.assertEqual(res, Solution().solve(s))
    def test_1(self):
        s = [['O','X','X','O','X'],['X','O','O','X','O'],['X','O','X','O','X'],['O','X','O','O','O'],['X','X','O','X','O']]
        res = [['O','X','X','O','X'],['X','X','X','X','O'],['X','X','X','O','X'],['O','X','O','O','O'],['X','X','O','X','O']]
        #print(Solution().solve(s))
        self.assertEqual(res, Solution().solve(s))

if __name__ == "__main__":
    unittest.main()