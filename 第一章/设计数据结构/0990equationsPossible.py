#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################
'''
990. Satisfiability of Equality Equations
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.
Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.
 

Example 1:
Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

Example 2:
Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Example 3:
Input: ["a==b","b==c","a==c"]
Output: true

Example 4:
Input: ["a==b","b!=c","c==a"]
Output: false

Example 5:
Input: ["c==c","b==d","x!=z"]
Output: true
 

Note:
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] and equations[i][3] are lowercase letters
equations[i][1] is either '=' or '!'
equations[i][2] is '='
'''

import unittest
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        uf = UF(26)
        # 先让相等的字母形成连通分量
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0])
                y = ord(eq[3])
                uf.union(x - ord('a'), y - ord('a'))

        # 检查不等关系是否打破相等关系的连通性
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0])
                y = ord(eq[3])
                # 如果相等关系成立，就是逻辑冲突
                if uf.connected(x - ord('a'), y - ord('a')):
                    return False

        return True
class UF(object):
    def __init__(self,n):
        #记录连通分量个数
        self.count = n
        print(self.count)
        #存储若干棵树
        self.parent = [i for i in range(n)]
        #记录树的“重量”
        self.size = [1 for i in range(n)]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return 
        #小树接到大树下面，较平衡
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = self.parent[rootP]
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = self.parent[rootQ]
            self.size[rootQ] += self.size[rootP]
        self.count -= 1
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ
    def find(self,x):
        
        while self.parent[x] != x:
            #进行路径压缩
            self.parent[x] = self.parent[self.parent[x]]
            x= self.parent[x]
        
        return x
    def getCount(self):
        return self.count
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = ["a==b","b!=a"]
        res = False
        self.assertEqual(res, Solution().equationsPossible(s))
    def test_1(self):
        s = ["b==a","a==b"]
        res = True
        self.assertEqual(res, Solution().equationsPossible(s))
    def test_2(self):
        s = ["a==b","b==c","a==c"]
        res = True
        self.assertEqual(res, Solution().equationsPossible(s))
    def test_3(self):
        s = ["a==b","b!=c","c==a"]
        res = False
        self.assertEqual(res, Solution().equationsPossible(s))

if __name__ == "__main__":
    unittest.main()