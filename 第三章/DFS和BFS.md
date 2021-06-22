# DFS和BFS

```
class Solution(object):
    def DFS(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path = []
        self.res = []
        self.backtrack(n, n, path)
        return self.res

    def backtrack(self, 选择列表, path):
        if not match:
            return
        if 满足结束条件:
            self.res.append(path[:])
            return

        for 选择 in 列表:
            # 选择
            path.append()
            self.backtrack(选择列表, path)
            # 撤销选择
            path.pop()
```



```
class Solution(object):
    def BFS(self, start, target):
        # 核心数据结构
        q = Queue.Queue()
        # 避免走回头路
        visited = set()
        # 将起点加入队列
        q.offer(start)
        visited.add(start)
        # 记录扩散的步数
        step = 0

        while not q.empty():
            sz = q.qsize()
            # 将当前队列中的所有节点向四周扩散
            for i in range(sz):
                cur = q.get()
                # 划重点：这里判断是否到达终点
                if cur is target:
                    return step
                # 将 cur 的相邻节点加入队列
                for x in cur.adj():
                    if x not in visited:
                        q.offer(x)
                        visited.add(x)

            step += 1
        return -1
class Solution(object):
    def BFS(self, start, target):
        # 双向BFS有局限，必须知道终点在哪里
        q1 = set()
        q2 = set()
        # 避免走回头路
        visited = set()
        # 将起点加入队列
        q1.add(start)
        q2.add(target)
        # 记录扩散的步数
        step = 0

        while q1 and q2:
            # 队列（集合）中的元素越多，扩散之后新的队列（集合）中的元素就越多；
            # 在双向BFS算法中，如果我们每次都选择一个较小的集合进行扩散，那么占用的空间增长速度就会慢一些，效率就会高一些    
            if len(q1) > len(q2):
                tmp = q1
                q1 = q2
                q2 = tmp
            # 哈希集合在遍历的过程中不能修改，用 temp 存储扩散结果
            temp = set()
            # 将 q1 中的所有节点向周围扩散
            for cur in q1:
                if cur in q2:
                    return step
                visited.add(cur)
                # 将 cur 的相邻节点加入队列
                for x in cur.adj():
                    if x not in visited:
                        temp.add(x)

            step += 1
            # temp 相当于 q1, 这里交换 q1 q2，下一轮 while 就是扩散 q2
            q1 = q2
            q2 = tmp
        return -1
```

