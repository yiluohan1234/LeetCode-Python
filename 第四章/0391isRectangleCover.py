#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: 1097189275@qq.com
#    > Created Time: 2021年5月12日
#    > description: 
#######################################################################
'''
391. 完美矩形(https://leetcode-cn.com/problems/perfect-rectangle/)
我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。
每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。


示例 1:
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
'''
import unittest
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        X1, Y1 = float('inf'), float('inf')
        X2, Y2 = -float('inf'), -float('inf')
    
        points = set()
        actual_area = 0
        for x1, y1, x2, y2 in rectangles:
            # 计算完美矩形的理论顶点坐标
            X1, Y1 = min(X1, x1), min(Y1, y1)
            X2, Y2 = max(X2, x2), max(Y2, y2)
            # 累加小矩形的面积
            actual_area += (x2 - x1) * (y2 - y1)
            # 记录最终形成的图形中的顶点
            p1, p2 = (x1, y1), (x1, y2)
            p3, p4 = (x2, y1), (x2, y2)
            for p in [p1, p2, p3, p4]:
                if p in points: 
                    points.remove(p)
                else:           
                    points.add(p)
        # 判断面积是否相同
        expected_area = (X2 - X1) * (Y2 - Y1)
        if actual_area != expected_area:
            return False
        # 判断最终留下的顶点个数是否为 4
        if len(points) != 4:       
            return False
        # 判断留下的 4 个顶点是否是完美矩形的顶点
        if (X1, Y1) not in points: return False
        if (X1, Y2) not in points: return False
        if (X2, Y1) not in points: return False
        if (X2, Y2) not in points: return False
        # 面积和顶点都对应，说明矩形符合题意
        return True
        
        
class TestSolution(unittest.TestCase):
    def test_0(self):
        rectangles = [
          [1,1,3,3],
          [3,1,4,2],
          [3,2,4,4],
          [1,3,2,4],
          [2,3,3,4]
        ]
        res = True
        self.assertEqual(res, Solution().isRectangleCover(rectangles))

if __name__ == "__main__":
    unittest.main()
