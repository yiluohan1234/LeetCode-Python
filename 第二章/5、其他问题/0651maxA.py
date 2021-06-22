#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月1日
#    > description: 
#######################################################################
import unittest
class Solution(object):
    def maxA(self, N):
        # 备忘录
        memo = dict()
        # 第一个状态n：剩余的按键次数；第二个状态a_num：当前屏幕上字符 A的数量；第三个状态copy：剪切板中字符 A的数量。
        def dp(n, a_num, copy):
            if n <= 0: return a_num;
            # 避免计算重叠子问题
            if (n, a_num, copy) in memo:
                return memo[(n, a_num, copy)]
    
            memo[(n, a_num, copy)] = max(
                    dp(n-1, a_num+1, copy),     # A
                    dp(n-1, a_num+copy, copy),  # C-V
                    dp(n-2, a_num, a_num)       # C-A C-C，剪切板中 A 的数量变为屏幕上 A 的数量
                )
            return memo[(n, a_num, copy)]
    
        return dp(N, 0, 0)
    def maxA1(self, N):
        dp = [0 for _ in range(N+1)]
        for i in range(1, N+1):
            # 按A键
            dp[i] = dp[i-1]+1
            for j in range(2, i):
                # 全选 &复制dp[j-2],连续粘贴i-j次
                dp[i] = max(dp[i], dp[j-2]*(i-j+1))
        
        return dp[N]
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 3
        res = 3
        self.assertEqual(res, Solution().maxA1(s))
    def test_1(self):
        s = 7
        res = 9
        self.assertEqual(res, Solution().maxA1(s))

if __name__ == '__main__':
    unittest.main()
    
