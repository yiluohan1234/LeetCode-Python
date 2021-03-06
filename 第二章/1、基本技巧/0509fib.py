#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年6月10日
#    > description: 
#######################################################################
'''
[509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。
f(n) = 1, n=1, 2
       f(n-1) + f(n-2) , n >2
零、动态规划问题框架：
动态规划问题的一般形式就是求最值。它其实是一种运筹学的一种最优化的方法。
求最值，核心问题是什么？求解动态规划的核心问题是穷举。
首先，动态规划问题存在「重叠子问题」，暴力穷举效率极其低下，需要「备忘录」或者「DP table」来优化穷举过程，避免不必要的计算。
其次，动态规划问题，一定会具备「最优子结构」，才能通过子问题的最值得到原问题的最值。要符合「最优子结构」，子问题间必须互相独立。
另外，虽然动态规划的核心思想就是穷举求最值，但是问题可以千变万化，穷举所有可行解其实并不是一件容易的事，只有列出正确的「状态转移方程」才能正确地穷举。

重叠子问题、最优子结构、状态转移方程就是动态规划三要素。
「最优子结构」是某些问题的一种特定性质，并不是动态规划问题专有的。
动态规划不就是从最简单的 base case 往后推导吗，可以想象成一个链式反应，不断以小博大。但只有符合最优子结构的问题，才有发生这种链式反应的性质。
找最优子结构的过程，其实就是证明状态转移方程正确性的过程，方程符合最优子结构就可以写暴力解了，写出暴力解就可以看出有没有重叠子问题了，有则优化，无则 OK。

递归问题，列出递归树，有助于分析算法的复杂度，寻找算法低效的原因。
递归算法的时间复杂度怎么计算？子问题个数乘以解决一个子问题需要的时间。
存在重复计算：设定一个「备忘录」，每次算出某个子问题的答案后别急着返回，先记到「备忘录」里再返回；
每次遇到一个子问题先去「备忘录」里查一查，如果发现之前已经解决过这个问题了，直接把答案拿出来用，不要再耗时去计算了。
备忘录的初始值也可以作为是否越界的标准。备忘录的初始值可以是不能取到的值N（如-1），如果备忘录的值不等于设定的初始值N，就放回记录的值。如果等于初始值则，没有进行备忘或越界了。
带「备忘录」的递归算法，把一棵存在巨量冗余的递归树通过「剪枝」，改造成了一幅不存在冗余的递归图，极大减少了子问题（即递归图中节点）的个数。

递归方法叫做「自顶向下」，动态规划叫做「自底向上」。
递归算法->带备忘录的递归算法->dp数组的迭代解法。

实际上带备忘录的递归解法中的「备忘录」，最终完成后就是这个 DP table。其实，状态转移方程直接代表着暴力解法。
千万不要看不起暴力解，动态规划问题最困难的就是写出状态转移方程，即这个暴力解。优化方法无非是用备忘录或者 DP table，再无奥妙可言。
当动态规划中的状态为固定值时（如斐波那契数列中，当前状态仅和两个状态有关），可以通过固定变量来进行状态变化，不需要建立 DP table。

如果遇到最优子结构失效的情况，怎么办？策略是：改造问题。不同的最优子结构，可能导致不同的解法和效率。

一、写状态方程是最困难的，如何写出状态方程：
明确「状态」 -> 定义 dp 数组/函数的含义 -> 明确「选择」并择优-> 明确 base case。
1、明确「状态」。原问题和子问题中变化的变量。
2、定义 dp 数组/函数的含义。
3、明确「选择」并择优。对于每个状态，可以做出什么选择改变当前状态。
4、明确 base case。

二、怎么确定dp数组的遍历方向？
以dp二维数组为例，有时正向遍历，有时反向遍历，有时斜向遍历。
1、遍历的过程中，所需的状态必须是已经计算出来的。
2、遍历的终点必须是存储结果的那个位置。

三、动态规划的降为打击：状态压缩。
「状态压缩」技巧能把很多动态规划解法的空间复杂度进一步降低，由 O(N^2) 降低到 O(N)，

能够使用状态压缩技巧的动态规划都是二维dp问题，你看它的状态转移方程：
如果计算状态dp[i][j]需要的都是dp[i][j]相邻的状态，那么就可以使用状态压缩技巧，将二维的dp数组转化成一维，将空间复杂度从 O(N^2) 降低到 O(N)。

例如前文最长回文子序列中：
```
for (int i = n - 2; i >= 0; i--) {
    for (int j = i + 1; j < n; j++) {
        // 状态转移方程
        if (s[i] == s[j])
            dp[i][j] = dp[i + 1][j - 1] + 2;
        else
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
    }
}
```
dp[i][j]的更新，其实只依赖于dp[i+1][j-1], dp[i][j-1], dp[i+1][j]这三个状态
状态压缩的核心思路就是，将二维数组「投影」到一维数组：
思路很直观，但是也有一个明显的问题，图中dp[i][j-1]和dp[i+1][j-1]这两个状态处在同一列，
而一维数组中只能容下一个，那么当我计算dp[i][j]时，他俩必然有一个会被另一个覆盖掉，怎么办？
1、一般来说是把第一个维度，也就是i这个维度去掉，只剩下j这个维度。压缩后的一维dp数组就是之前二维dp数组的dp[i][..]那一行。
```
for (int i = n - 2; i >= 0; i--) {
    for (int j = i + 1; j < n; j++) {
        // 在这里，一维 dp 数组中的数是什么？
        if (s[i] == s[j])
            dp[j] = dp[j - 1] + 2;
        else
            dp[j] = max(dp[j], dp[j - 1]);
    }
}
```
2、上述代码的一维dp数组只能表示二维dp数组的一行dp[i][..]，那我怎么才能得到dp[i+1][j-1], dp[i][j-1], dp[i+1][j]这几个必要的的值，进行状态转移呢？
在代码中注释的位置，将要进行状态转移，更新dp[j]，那么我们要来思考两个问题：

1)在对dp[j]赋新值之前，dp[j]对应着二维dp数组中的什么位置？
2)dp[j-1]对应着二维dp数组中的什么位置？

对于问题 1，在对dp[j]赋新值之前，dp[j]的值就是外层 for 循环上一次迭代算出来的值，也就是对应二维dp数组中dp[i+1][j]的位置。
对于问题 2，dp[j-1]的值就是内层 for 循环上一次迭代算出来的值，也就是对应二维dp数组中dp[i][j-1]的位置。
那么问题已经解决了一大半了，只剩下二维dp数组中的dp[i+1][j-1]这个状态我们不能直接从一维dp数组中得到。
```
for (int i = n - 2; i >= 0; i--) {
    for (int j = i + 1; j < n; j++) {
        if (s[i] == s[j])
            // dp[i][j] = dp[i+1][j-1] + 2;
            dp[j] = ?? + 2;
        else
            // dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
            dp[j] = max(dp[j], dp[j - 1]);
    }
}
```
遍历顺序为从左向右，从下向上。dp[i+1][j] -> d[i+1][j-1] -> dp[i][j-1]-> dp[i][j]
三、那么如果我们想得到dp[i+1][j-1]，就必须在它被覆盖之前用一个临时变量temp把它存起来，并把这个变量的值保留到计算dp[i][j]的时候
```
for (int i = n - 2; i >= 0; i--) {
    // 存储 dp[i+1][j-1] 的变量
    int pre = 0;
    for (int j = i + 1; j < n; j++) {
        int temp = dp[j];
        if (s[i] == s[j])
            // dp[i][j] = dp[i+1][j-1] + 2;
            dp[j] = pre + 2;
        else
            dp[j] = max(dp[j], dp[j - 1]);
        // 到下一轮循环，pre 就是 dp[i+1][j-1] 了
        pre = temp;
    }
}
```

'''
import unittest
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        # 暴力递归解法（自顶而下）
        if n == 1 or n == 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)
    
    def fib1(self, n):
        # 带备忘录的暴力递归解法（自顶而下）
        if n < 0:
            return 0
        memo = [0 for _ in range(n+1)]
        return self.Helper(memo, n)
    def Helper(self, memo, n):
        if n == 1 or n == 2:
            return 1
        if memo[n] != 0:
            return memo[n]
        memo[n] = self.Helper(memo, n-1) + self.Helper(memo, n-2)
        
        return memo[n]
    def fib2(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        # dp 数组迭代解法（自底而上）
        dp = [0 for _ in range(n+1)]
        dp[1] = dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 4
        res = 3
        self.assertEqual(res, Solution().fib2(s))

if __name__ == "__main__":
    unittest.main()
