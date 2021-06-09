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
今天讲讲 Union-Find 算法，也就是常说的并查集算法，主要是解决图论中「动态连通性」问题的。
算法的关键点有 3 个：
1、用parent数组记录每个节点的父节点，相当于指向父节点的指针，所以parent数组内实际存储着一个森林（若干棵多叉树）
2、用size数组记录着每棵树的重量，目的是让union后树依然拥有平衡性，而不会退化成链表，影响操作效率。
3、在find函数中进行路径压缩，保证任意树的高度保持在常数，使得union和connectedAPI 时间复杂度为 O(1)。
'''
import unittest
class UF(object):
    def __init__(self,n):
        #记录连通分量个数
        self.count = n
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
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, UF().intToRoman(s))

if __name__ == "__main__":
    unittest.main()