#!/usr/bin/env python
# coding=utf-8
#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File    : 0142detectCycle.py
#    > Version : 1.0
#    > Author  : Cui Yufei 
#    > Email   : 1097189275@qq.com
#    > Time    : 2021/08/19 10:37:47
#    > License : (C)Copyright 2017-2018, XXX
#    > Desc    : None
#######################################################################
'''
[142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。
进阶：
你是否可以使用 O(1) 空间解决此题？

''' 
import unittest
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 我们假设快慢指针相遇时，慢指针slow走了k步，那么快指针fast一定走了2k步
        # 假设相遇点距环的起点的距离为m，那么环的起点距头结点head的距离为k - m，也就是说如果从head前进k - m步就能到达环起点。巧的是，如果从相遇点继续前进k - m步，也恰好到达环起点
        slow, fast = head, head 
        while fast != None and fast.next != None:
            slow = slow.next 
            fast =fast.next.next 
            if slow == fast:
                break 
        # 上面的代码类似 hasCycle 函数
        if fast == None or fast.next == None:
            # fast 遇到空指针说明没有环
            return None 

        # 重新指向头结点
        slow = head 
        # 快慢指针同步前进，相交点就是环起点
        while slow != fast :
            slow = slow.next 
            fast = fast.next 
        
        return slow 
    

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = 1994
        res = "MCMXCIV"
        self.assertEqual(res, Solution().intToRoman(s))

if __name__ == "__main__":
    unittest.main()