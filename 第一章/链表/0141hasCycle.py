#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0141hasCycle.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/19 10:27:05
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################

'''
[141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

''' 
import unittest
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 快慢指针初始化指向 head
        slow, fast = head, head 
        # 快指针走到末尾时停止
        while fast != None and fast.next != None:
            slow = slow.next 
            fast =fast.next.next 
            # 快慢指针相遇，说明含有环
            if slow == fast:
                return True 
        
        return False
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()