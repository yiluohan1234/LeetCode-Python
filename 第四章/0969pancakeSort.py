#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: pancakeSort.py
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月10日
#    > description: 
#######################################################################
'''
[969. 煎饼排序](https://leetcode-cn.com/problems/pancake-sorting/)

给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。

一次煎饼翻转的执行过程如下：

选择一个整数 k ，1 <= k <= arr.length
反转子数组 arr[0...k-1]（下标从 0 开始）
例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。

以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * arr.length 范围内的有效答案都将被判断为正确。

 

示例 1：                
输入：[3,2,4,1]
输出：[4,2,4,3]
解释：
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 arr = [3, 2, 4, 1]
第一次翻转后（k = 4）：arr = [1, 4, 2, 3]
第二次翻转后（k = 2）：arr = [4, 1, 2, 3]
第三次翻转后（k = 4）：arr = [3, 2, 1, 4]
第四次翻转后（k = 3）：arr = [1, 2, 3, 4]，此时已完成排序。 

'''
import unittest
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        self.res = []
        
        self.sort_arr(arr, len(arr))
        return self.res
    def sort_arr(self, arr, n):
        if n == 1:
            return
        maxidx = 0
        maxvalue = 0
        # 每次查找缩小范围内的最大值
        for i in range(n):
            if arr[i] > maxvalue:
                maxidx = i
                maxvalue = arr[i]
        self.reverse_arr(arr, 0, maxidx)
        self.res.append(maxidx+1)
        self.reverse_arr(arr, 0, n-1)
        self.res.append(n)
        
        self.sort_arr(arr, n-1)
    def reverse_arr(self, arr, i, j):
        while i < j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1
class Solution1(object):
    def pancakeSort(self, arr):
        if not arr:
            return []
        res = []
        idx = arr.index(max(arr))
        # 第一次翻转
        arr = arr[:idx+1][::-1] + arr[idx+1:]
        # 第二次翻转
        arr = arr[::-1]
        res += [idx+1, len(arr)]
        temp = self.pancakeSort(arr[:-1])
        res = res + temp
        return res


  
class TestSolution(unittest.TestCase):
    def test_0(self):
        s = [3,2,4,1]
        res = [4,2,4,3]
        self.assertEqual(res, Solution().pancakeSort1(s))

if __name__ == "__main__":
#     unittest.main()
    s = [3,2,4,1]
    print(s[:2])
    
    