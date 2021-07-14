#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0032longestValidParentheses.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/07/13 09:34:40
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
32. 最长有效括号(https://leetcode-cn.com/problems/longest-valid-parentheses/)
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
'''
import unittest
class Solution(object):
    def longestValidParentheses0(self, s):
        # 既然我们要找满足匹配规则的子串，那肯定要以左括号"("开始进行查找啊对吧？我们遍历s，将左括号的下标保存成一个数组nums。
        # 这时，如果数组长度等于s,那return 0即可。
        # 接下来我们开始循环nums，从每一个左括号开始进行查找。
        # 如果left == right的数量比较最大值ret=max(ret,left * 2)。
        # 如果right > left，停止，从下一个左括号下标继续找起。
        lg = len(s)
        nums = [i for i in range(lg) if s[i] == '(']
        if len(nums) == lg:
            return 0
        ret = 0
        for left in nums:
            a, b = 0, 0
            for i in range(left, lg):
                if s[i] == '(':
                    a += 1
                else:
                    b += 1
                if a == b:
                    ret = max(ret, a * 2)
                elif b > a:
                    break
        return ret
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 初始栈为stack = [-1]即哨兵节点，这个是老套路..., 然后开始遍历s的下标, 当s[i]为左括号时，无脑入栈 ,当s[i]为右括号时, 我们先pop栈顶
        # 如果栈为空，则我们将哨兵pop掉了，没有正确匹配，将当前的i压栈继续当哨兵。
        # 当pop出的栈顶为左括号，那么更新ret = max(ret, i- 此时栈顶)
        # 重复3、4操作，即可获取最终结果
        if not s:
            return 0
        ret = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ret = max(ret, i - stack[-1])
        return ret
    def longestValidParentheses1(self, s):
        # 下面谈谈贪心思路，其实暴力解法通过的时候，我们就该考虑贪心的，因为我们做了很多重复的查找。
        # 当我们发现右括号大于左括号的时候，我们break后，就可以从当前位置开始找下一个左括号了。
        # 所以利用贪心，我们通过边循环变更新的思路，可以减少重复的查找。
        #初始left = right = 0，然后循环s
        #当left == right，更新ret
        #当right > left,那前面的数据都是报废且计算过最大值得，全部舍弃掉，重复1操作。
        #这样就完了吗？不是，我们只判断了right > left,那如果left一直大于right呢？换位思考是不颠倒左右括号就能实现这种异常场景... 
        # 所以，我们从右向左再遍历一次s，就能解决这个问题了。

        #这里有个小tips，从左向右，从右向左，代码都是一样的，知识判断r > l 和 l > r的条件不一样。
        # 有什么办法能复用这套查找代码呢？我们定义一个标记位，然后使用异或的判断就行。
        # 公式为：order ^ (left > right)初始order = True代表正序，然后计算left > right， 异或中True ^ True为False。
        # 只有当True ^ False时才为True，执行重置 倒序遍历时一样，order = False 但是left > right 一直是False，False ^ False为False。
        # 这样就能实现代码的复用了，这个操作是不是很骚？
        def comp(strings, order=True):
            ret = 0
            left = right = 0
            for i in strings:
                if i == '(':
                    left += 1
                else:
                    right += 1
                if left == right:
                    ret = max(ret, left * 2)
                elif order ^ (left > right):
                    left = right = 0
            return ret
        return max(comp(s), comp(s[::-1], False))
       
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = "(()"
        res = 2
        self.assertEqual(res, Solution().longestValidParentheses(s))
    def test_1(self):
        s = ")()())"
        res = 4
        self.assertEqual(res, Solution().longestValidParentheses(s))
    def test_1(self):
        s = ""
        res = 0
        self.assertEqual(res, Solution().longestValidParentheses(s))

if __name__ == '__main__':
    unittest.main()
    
