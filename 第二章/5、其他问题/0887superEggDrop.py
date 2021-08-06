#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月31日
#    > description: 
#######################################################################
'''
[887. 鸡蛋掉落](https://leetcode-cn.com/problems/super-egg-drop/)
给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

 
示例 1：
输入：k = 1, n = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。 
否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。 
如果它没碎，那么肯定能得出 f = 2 。 
因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。 
'''
import unittest
class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        # 这种方法会超时
        meno = {}
        # 定义：当前状态为 k 个鸡蛋，面对 n 层楼, 返回这个状态下最少的扔鸡蛋次数
        # 状态：如果鸡蛋碎了，那么鸡蛋的个数K应该减一，搜索的楼层区间应该从[1..N]变为[1..i-1]共i-1层楼；
        #     如果鸡蛋没碎，那么鸡蛋的个数K不变，搜索的楼层区间应该从 [1..N]变为[i+1..N]共N-i层楼。
        def dp(K,N):
            if K == 1:
                return N 
            if N == 0:
                return 0
            res = float('inf')
            for i in range(1, N+1):
                # 最坏情况下的最少扔鸡蛋次数
                res = min(res,
                          max(dp(K-1, i-1), # 碎
                              dp(K, N - i)) #没碎
                          +1)
            meno[(K, N)] = res
            return res
        return dp(k, n)
    def superEggDrop1(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        meno = {}
        # 定义：当前状态为 k 个鸡蛋，面对 n 层楼, 返回这个状态下最少的扔鸡蛋次数
        # 状态：如果鸡蛋碎了，那么鸡蛋的个数K应该减一，搜索的楼层区间应该从[1..N]变为[1..i-1]共i-1层楼；
        #     如果鸡蛋没碎，那么鸡蛋的个数K不变，搜索的楼层区间应该从 [1..N]变为[i+1..N]共N-i层楼。
        def dp(K,N):
            if K == 1:
                return N 
            if N == 0:
                return 0
            res = float('inf')
#             for i in range(1, N+1):
#                 res = min(res,
#                           max(dp(K-1, i-1), # 碎
#                               dp(K, N - i)) #没碎
#                           +1)
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken+1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken+1)
                
            meno[(K, N)] = res
            return res
        return dp(k, n)
    def superEggDrop2(self, k, n):
        # 当前有 k 个鸡蛋，可以尝试扔 m 次鸡蛋， 这个状态下，最坏情况下最多能确切测试一栋 n 层的楼
        # 比如说 dp[1][7] = 7 表示：
        # 现在有 1 个鸡蛋，允许你扔 7 次;
        # 这个状态下最多给你 7 层楼，
        # 使得你可以确定楼层 F 使得鸡蛋恰好摔不碎
        # （一层一层线性探查嘛）
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
        m = 0
        while dp[k][m] < n:
            m += 1
            for k in range(1, k+1):
                # 基于下面两个事实：
                # 1、无论你在哪层楼扔鸡蛋，鸡蛋只可能摔碎或者没摔碎，碎了的话就测楼下，没碎的话就测楼上。
                # 2、无论你上楼还是下楼，总的楼层数 = 楼上的楼层数 + 楼下的楼层数 + 1（当前这层楼）。
                # 状态转移方程：dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
                dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
        
        return m
    def superEggDrop3(self, k, n):
        # 当前有 k 个鸡蛋，可以尝试扔 m 次鸡蛋， 这个状态下，最坏情况下最多能确切测试一栋 n 层的楼
        # 比如说 dp[1][7] = 7 表示：
        # 现在有 1 个鸡蛋，允许你扔 7 次;
        # 这个状态下最多给你 7 层楼，
        # 使得你可以确定楼层 F 使得鸡蛋恰好摔不碎
        # （一层一层线性探查嘛）
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
        lo, hi = 1, n
        while lo < hi:
            mid = (lo+hi)//2
            if ...< n:
                lo = ...
            else:
                hi = ...

            for k in range(1, k+1):
                dp[k][mid] = dp[k][mid-1] + dp[k-1][mid-1] + 1
        
        return mid
class TestSolution(unittest.TestCase):
    def test_0(self):
        k = 1
        n = 2
        res = 2
        self.assertEqual(res, Solution().superEggDrop3(k, n))
    def test_1(self):
        k = 2
        n = 6
        res = 3
        self.assertEqual(res, Solution().superEggDrop3(k, n))
    def test_2(self):
        k = 3
        n = 14
        res = 4
        self.assertEqual(res, Solution().superEggDrop3(k, n))

if __name__ == '__main__':
    unittest.main()