#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月18日
#    > description: 
#######################################################################
'''
输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
输出：[null,0,9,4,2,null,5]
解释：
ExamRoom(10) -> null
seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
seat() -> 9，学生最后坐在 9 号座位上。
seat() -> 4，学生最后坐在 4 号座位上。
seat() -> 2，学生最后坐在 2 号座位上。
leave(4) -> null
seat() -> 5，学生最后坐在 5 号座位上。
'''
import unittest
from sortedcontainers import SortedListWithKey
class ExamRoom:

    def __init__(self, N):
        self.N = N
        self.p = {-1:(-1, N)}
        self.q = {N: (-1, N)}
        # 如果距离相同，选序号最小的
        self.pq = SortedListWithKey([(-1, N)], key=lambda x: (self.distance(x[0], x[1]), -x[0])) 
    
    def distance(self, a, b):
        if a == -1:
            return b
        if b == self.N:
            return self.N - 1 - a
        return (b - a) // 2

    def _remove(self, a, b):
        self.p.pop(a)
        self.q.pop(b)
        self.pq.remove((a, b))
    
    def _add(self, a, b):
        self.p[a] = (a, b)
        self.q[b] = (a, b)
        self.pq.add((a, b))

    def seat(self):
        a, b = self.pq[-1]
        if a == -1:
            p = 0
        elif b == self.N:
            p = self.N-1
        else:
            p = (b - a) // 2 + a
        
        self._remove(a, b)
        self._add(a, p)
        self._add(p, b)
        return p

    def leave(self, p):
        la, lb = self.q[p]
        ra, rb = self.p[p]
        self._remove(la, lb)
        self._remove(ra, rb)
        self._add(la, rb)
    def reqp(self):
        return self.pq



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

    
if __name__ == "__main__":
    s = ExamRoom(10)
    print(s.seat())
    print(s.seat())
    print(s.seat())
    print(s.seat())
    print(s.leave(4))
    print(s.seat())
    print(s.seat())
    print(s.reqp())
