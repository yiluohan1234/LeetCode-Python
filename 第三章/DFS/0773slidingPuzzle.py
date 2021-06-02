#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年4月6日
#    > description: 
#######################################################################
'''
[773. 滑动谜题](https://leetcode-cn.com/problems/sliding-puzzle/)
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
'''
import unittest
import queue
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        start = ""
        target = "123450"
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        # ******* BFS 算法框架开始 *******
        q = queue.Queue()
        visited = set()
        step = 0
        q.put(start)
        visited.add(start)
        neighbor = [
            [1,3],
            [0,4,2],
            [1,5],
            [0,4],
            [3,1,5],
            [2,4]
        ]
        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                cur = q.get()
                # 判断是否达到目标局面
                if cur == target:
                    return step
                idx = 0
                while cur[idx] != '0':
                    idx += 1
                for adj in neighbor[idx]:
                    # 将数字 0 和相邻的数字交换位置
                    new_board_list = [c for c in cur]
                    tmp = new_board_list[adj]
                    new_board_list[adj] = new_board_list[idx]
                    new_board_list[idx] = tmp
                    new_board = "".join(new_board_list)
                    if new_board not in visited:
                        q.put(new_board)
                        visited.add(new_board)
            step += 1
        
        return -1

class Solution2(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        start = ""
        target = "123450"
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        # ******* BFS 算法框架开始 *******
        q1 = set()
        q2 = set()
        visited = set()
        step = 0
        q1.add(start)
        q2.add(target)
        neighbor = [
            [1,3],
            [0,4,2],
            [1,5],
            [0,4],
            [3,1,5],
            [2,4]
        ]            
        while q1 and q2:
            if len(q1) > len(q2):
                tmp = q1
                q1 = q2
                q2 = tmp
            # 哈希集合在遍历的过程中不能修改，用 temp 存储扩散结果
            temp = set()
            # 将 q1 中的所有节点向周围扩散
            for cur in q1:
                # 判断是否到达终点
                if cur in q2:
                    return step
                visited.add(cur)
                idx = 0
                while cur[idx] != '0':
                    idx += 1
                # 将一个节点的未遍历相邻节点加入集合
                for adj in neighbor[idx]:
                    # 将数字 0 和相邻的数字交换位置
                    new_board_list = [c for c in cur]
                    tmp = new_board_list[adj]
                    new_board_list[adj] = new_board_list[idx]
                    new_board_list[idx] = tmp
                    new_board = "".join(new_board_list)
                    if new_board not in visited:
                        temp.add(new_board)
            step += 1
            # temp 相当于 q1, 这里交换 q1 q2，下一轮 while 就是扩散 q2
            q1 = q2
            q2 = temp
        return -1
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        board = [[4,1,2],[5,0,3]]
        res = 5
        self.assertEqual(res, Solution2().slidingPuzzle(board))
    def test_1(self):
        board = [[1,2,3],[4,0,5]]
        res = 1
        self.assertEqual(res, Solution2().slidingPuzzle(board))
    def test_2(self):
        board = [[1,2,3],[5,4,0]]
        res = -1
        self.assertEqual(res, Solution2().slidingPuzzle(board))
    def test_3(self):
        board = [[3,2,4],[1,5,0]]
        res = 14
        self.assertEqual(res, Solution2().slidingPuzzle(board))
if __name__ == "__main__":
    unittest.main()