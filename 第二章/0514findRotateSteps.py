#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月3日
#    > description: 
#######################################################################
'''
514. 自由之路(https://leetcode-cn.com/problems/freedom-trail/)
电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。
旋转 ring 拼出 key 字符 key[i] 的阶段中：
您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。
示例：
输入: ring = "godding", key = "gd"
输出: 4
解释:
 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。 
 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
 当然, 我们还需要1步进行拼写。
 因此最终的输出是 4。
 '''
import unittest
class Solution(object):
    def __init__(self):
        self.charToIndex = {}
        self.memo = {}
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        # 字典中值为列表的构造方法
        # dic = {}
        # dic.setdefault(key,[]).append(value)    
        
        m = len(ring)
        n = len(key)
        # 备忘录全部初始化为 0
        #memo.resize(m, vector<int>(n, 0));
        # 记录圆环上字符到索引的映射
        for i in range(m):
            self.charToIndex.setdefault(ring[i],[]).append(i)
            #self.charToIndex[ring[i]].push_back(i)
        # 圆盘指针最初指向 12 点钟方向，
        # 从第一个字符开始输入 key
        return self.dp(ring, 0, key, 0)

    # 计算圆盘指针在 ring[i]，输入 key[j..] 的最少操作数
    def dp(self, ring, i, key, j):
        # base case 完成输入
        if j == len(key): 
            return 0
        # 查找备忘录，避免重叠子问题
        if (i,j) in self.memo:
            return self.memo[(i,j)]
        
        n = len(ring)
        # 做选择
        res = float('inf')
        # ring 上可能有多个字符 key[j]
        for k in self.charToIndex[key[j]]:
            # 拨动指针的次数
            delta = abs(k - i)
            # 选择顺时针还是逆时针
            delta = min(delta, n - delta);
            # 将指针拨到 ring[k]，继续输入 key[j+1..]
            subProblem = self.dp(ring, k, key, j + 1)
            # 选择「整体」操作次数最少的
            res = min(res, 1 + delta + subProblem)
            # PS：加一是因为按动按钮也是一次操作
        # 将结果存入备忘录
        self.memo[(i,j)] = res
        return res
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        ring = "godding"
        key = "gd"
        res = 4
        self.assertEqual(res, Solution().findRotateSteps(ring, key))

if __name__ == '__main__':
    unittest.main()
    
