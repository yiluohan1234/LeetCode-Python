#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2021年3月27日
#    > description: 
#######################################################################
'''
[698. 划分为k个相等的子集](https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/)
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
'''
import unittest
class Solution2(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k > len(nums):
            return False
        sum = 0
        for n in nums:
            sum += n
        if sum % k != 0:
            return False
        
        target = sum / k 
        bucket = [0 for i in range(k)]
        return self. backtrack(nums, 0, bucket, target)
    def backtrack(self, nums, index, bucket, target):
        if index == len(nums):
            for i in range(len(bucket)):
                if bucket[i] != target:
                    return False
            
            return True
        
        for i in range(len(bucket)):
            if nums[index] + bucket[i] > target:
                continue
            bucket[i] += nums[index]
            if self.backtrack(nums, index+1, bucket, target):
                return True
            
            bucket[i] -= nums[index]
        
        return False
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k > len(nums):
            return False
        sum, max_val = 0, 0
        for v in nums:
            sum += v
            if max_val < v:
                max_val = v
        target = sum / k
        if sum % k != 0 or max_val > target:
            return False
        used = [False for i in range(len(nums))]
        return self.backtrack(k, nums, 0, 0, used, target)
    def backtrack(self, k, nums, start, bucket_sum, used, target):
        if k == 0:
            return True
        if bucket_sum > target:
            return False
        if bucket_sum == target:
            return self.backtrack(k-1, nums, 0, 0, used, target)
        for i in range(start, len(nums)):
#             if used [i] or bucket_sum + nums[i] > target:
#                 continue
#             if bucket_sum + nums[i] > target:
#                 continue
#             if used[i]:
#                 continue 
#             if used [i] or i + 1 < len(nums) and nums[i] == nums[i + 1] and not used[i + 1]:
#                 continue
            if not used[i] or bucket_sum + nums[i] <= target:
                bucket_sum += nums[i]
                used[i] = True
                if self.backtrack(k, nums, i + 1, bucket_sum, used, target):
                    return True
                bucket_sum -= nums[i]
                used[i] = False
        return False
class Solution3(object):
    def canPartitionKSubsets(self, nums, k):
        target, reminder = divmod(sum(nums), k)
        if reminder or max(nums) > target: return False
        visited = [False] * len(nums)
        def DFS(k, index, cur_sum):
            print(cur_sum, index, end=' ')
            if k == 0:
                return True
            if cur_sum == target:
                return DFS(k-1, 0, 0)
            for i in range(index, len(nums)):
                # print(i)
                if cur_sum + nums[i] <= target and not visited[i]:
                    visited[i] = True
                    # print(i)
                    if DFS(k, i+1, cur_sum+nums[i]):
                        return True
                    visited[i] = False
            return False
            
            
        return DFS(k, 0, 0)
class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [4, 3, 2, 3, 5, 2, 1]
        k = 4
        res = True
        self.assertEqual(res, Solution().canPartitionKSubsets(nums, k))
    def test_1(self):
        nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,3,3]
        k = 8
        res = False
 
        self.assertEqual(res, Solution().canPartitionKSubsets(nums, k))
    def test_2(self):
        nums = [1,2,3,4] 
        k = 3
        res = False
 
        self.assertEqual(res, Solution().canPartitionKSubsets(nums, k))

    def test_3(self):
        nums = [2,2,2,2,3,4,5]
        k = 4
        res = False
        self.assertEqual(res, Solution().canPartitionKSubsets(nums, k))
    def test_4(self):
        nums = [1,1,1,1,1,1,1,1,1,1]
        k = 5
        res = True

        self.assertEqual(res, Solution().canPartitionKSubsets(nums, k))
if __name__ == "__main__":
#     unittest.main()
#     nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,3,3]
#     k = 8
#     print(Solution().canPartitionKSubsets(nums, k))
    print(chr(49))
