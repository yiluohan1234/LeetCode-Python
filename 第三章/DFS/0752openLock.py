#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 10971892@qq.com
#    > Created Time: 2021年4月5日
#    > description: 
#######################################################################
'''
[752. 打开转盘锁](https://leetcode-cn.com/problems/open-the-lock/)
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
'''
import unittest
import queue
'''
在python2.x中,模块名为Queue.Queue。python3直接queue.Queue即可
'''
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        q = queue.Queue()
        visited = set()
        step = 0
        q.put("0000")
        visited.add("0000")

        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                cur = q.get()
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                for j in range(4):
                    up = self.plusup(cur, j)
                    if up not in visited:
                        q.put(up)
                        visited.add(up)
                    down = self.plusdown(cur, j)
                    if down not in visited:
                        q.put(down)
                        visited.add(down)
            step += 1

        return -1
    def plusup(self, s, j):
        s_s = [c for c in s]
        if s_s[j] == '9':
            s_s[j] = '0'
        else:
            s_s[j] = chr(ord(s_s[j]) + 1)
        return "".join(s_s)
    def plusdown(self, s, j):
        s_s = [c for c in s]
        if s_s[j] == '0':
            s_s[j] = '9'
        else:
            s_s[j] = chr(ord(s_s[j]) - 1)
        return "".join(s_s)
class Solution2(object):
    # 不过，双向 BFS 也有局限，因为你必须知道终点在哪里
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """  
        # 用集合不用队列，可以快速判断元素是否存在
        q1 = set()
        q2 = set()
        visited = set()
        
        step = 0
        q1.add("0000")
        q2.add(target)
        
        while q1 and q2:
            # 队列（集合）中的元素越多，扩散之后新的队列（集合）中的元素就越多；
            # 在双向BFS算法中，如果我们每次都选择一个较小的集合进行扩散，那么占用的空间增长速度就会慢一些，效率就会高一些
            if len(q1) > len(q2):
                tmp = q1
                q1 = q2
                q2 = tmp
            # 哈希集合在遍历的过程中不能修改，用 temp 存储扩散结果
            tmp = set()
            # 将 q1 中的所有节点向周围扩散
            for cur in q1:
                # 判断是否到达终点
                if cur in deadends:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)
                # 将一个节点的未遍历相邻节点加入集合
                for j in range(4):
                    up = self.plusup(cur, j)
                    if up not in visited:
                        tmp.add(up)
                    down = self.plusdown(cur, j)
                    if down not in visited:
                        tmp.add(down)
            step += 1
            # temp 相当于 q1, 这里交换 q1 q2，下一轮 while 就是扩散 q2
            q1 = q2
            q2 = tmp
        return -1
    def plusup(self, s, j):
        s_s = [c for c in s]
        if s_s[j] == '9':
            s_s[j] = '0'
        else:
            s_s[j] = chr(ord(s_s[j]) + 1)
        return "".join(s_s)
    def plusdown(self, s, j):
        s_s = [c for c in s]
        if s_s[j] == '0':
            s_s[j] = '9'
        else:
            s_s[j] = chr(ord(s_s[j]) - 1)
        return "".join(s_s)
class TestSolution(unittest.TestCase):
    def test_0(self):
        deadends = ["0201","0101","0102","1212","2002"] 
        target = "0202"
        
        res = 6
        self.assertEqual(res, Solution2().openLock(deadends, target))
    def test_1(self):
        deadends = ["8888"]
        target = "0009"
        
        res = 1
        self.assertEqual(res, Solution2().openLock(deadends, target))
    def test_2(self):
        deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
        target = "8888"
        
        res = -1
        self.assertEqual(res, Solution2().openLock(deadends, target))
    def test_3(self):
        deadends = ["0000"]
        target = "8888"
        
        res = -1
        self.assertEqual(res, Solution2().openLock(deadends, target))
if __name__ == "__main__":
    unittest.main()