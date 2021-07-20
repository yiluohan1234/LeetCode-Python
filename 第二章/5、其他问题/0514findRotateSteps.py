#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0514findRotateSteps.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/15 16:22:32
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
514. 自由之路(https://leetcode-cn.com/problems/freedom-trail/)
电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。

最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。
旋转 ring 拼出 key 字符 key[i] 的阶段中：
您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。

'''
import unittest
import random
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(ring), len(key)
        self.chartoindex = {}
        self.memo = {}
        for i in range(m):
            c = ring[i]
            self.chartoindex.setdefault(c, []).append(i)
        return self.dp(ring, 0, key, 0)
    def longLIS(self, nums):
        top = {}
        piles = 0
        
        for i in range(len(nums)):
            poker = nums[i]
            lo, hi = 0, piles
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if top[mid] > poker:
                    hi = mid
                elif top[mid] < poker:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == piles:
                piles += 1
            top[lo] = poker
        
        return piles
    def dp(self, ring, i, key, j):
        # 计算圆盘指针在 ring[i]，输入 key[j..] 的最少操作数
        m, n = len(ring), len(key)
        if j == n:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        res = float('inf')

        # ring 上可能有多个字符 key[j]
        for k in self.chartoindex[key[j]]:
            # 拨动次数
            delta = abs(k-i)
            # 顺时针拨动还是逆时针拨动
            delta = min(delta, m - delta)
            sub_problem = self.dp(ring, k, key, j + 1)
            res = min(res, 1 + delta + sub_problem)
        self.memo[(i, j)] = res
        return res
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        ring = "godding"
        key = "gd"
        res = 4
        self.assertEqual(res, Solution().findRotateSteps(ring, key))

    def test_1(self):
        ring = "godding"
        key = "godding"
        res = 13
        self.assertEqual(res, Solution().findRotateSteps(ring, key))
    
if __name__ == '__main__':
    #unittest.main()
    # [0, 5, 4, 3, 2, 1, 0, -1]
    # [0, 1, 2, 3, 2, 1, 0, -1]
    # [0, 1, 4, 3, 2, 1, 6]
    blacklist = []
    N = 6
    for i in range(31):
        if random.randint(0, i) == 0:
            blacklist.append(i)
            i += 1
        else:
            blacklist.append(N - i)
        if i > N:
            if len(blacklist) == 6:
                break
        
    
    print(blacklist)