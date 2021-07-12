#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 1024videoStitching.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/12 15:18:13
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
1024. 视频拼接(https://leetcode-cn.com/problems/video-stitching/)
你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。

'''
import unittest
class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        # 按起点升序排列，起点相同的降序排列
        clips = sorted(clips, key=lambda x:(x[0], -x[1]))

        # 记录选择的短视频个数
        res = 0
        cur_end, next_end = 0, 0
        n = len(clips)
        i = 0
        while i < n and clips[i][0] <= cur_end:
            # 在第 res 个视频的区间内贪心选择下一个视频
            while i < n and clips[i][0] <= cur_end:
                next_end = max(next_end, clips[i][1])
                i += 1
            # 找到下一个视频，更新 curEnd
            res += 1
            cur_end = next_end
            if cur_end >= time:
                # 已经可以拼出区间 [0, T]
                return res 
        
        return -1

class TestSolution(unittest.TestCase):
    def test_0(self):
        clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
        T = 10
        res = 3
        self.assertEqual(res, Solution().videoStitching(clips, T))

    def test_1(self):
        clips = [[0,1],[1,2]]
        T = 5
        res = -1
        self.assertEqual(res, Solution().videoStitching(clips, T))
    def test_2(self):
        clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
        T = 9
        res = 3
        self.assertEqual(res, Solution().videoStitching(clips, T))
    def test_3(self):
        clips = [[0,4],[2,8]]
        T = 5
        res = 2
        self.assertEqual(res, Solution().videoStitching(clips, T))
    def test_4(self):
        clips = [[0,4],[2,8]]
        T = 5
        res = 2
        self.assertEqual(res, Solution().videoStitching(clips, T))

if __name__ == '__main__':
    unittest.main()