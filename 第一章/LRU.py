#!/usr/bin/env python
# coding=utf-8
#######################################################################
#    > File Name: 
#    > Author: cuiyufei
#    > Mail: XXX@qq.com
#    > Created Time: 2020年9月23日
#    > description: 
#######################################################################

import unittest
class Node(object):
    def __init__(self, k, v):
        """
        :type num: int
        :rtype: str
        """
        self.key = k 
        self.val = v 
        self.next = None
        self.prev = None

class DoubleList(object):
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def addLast(self, x):
        """在链表尾部添加节点 x，时间 O(1)
        """
        x.prev = self.tail.prev
        x.next = self.tail
        
        self.tail.prev.next = x 
        self.tail.prev = x
        self.size += 1
    
    def remove(self, x):
        """删除链表中的 x 节点（x 一定存在）,由于是双链表且给的是目标 Node 节点，时间 O(1)
        """
        x.prev.next = x.next 
        x.next.prev = x.prev
        self.size -= 1
        
    def removeFirst(self):
        """删除链表中第一个节点，并返回该节点，时间 O(1)
        """
        if self.head.next == self.tail:
            return
        first = self.head.next
        self.remove(first)
        return first
    
    def getSize(self):
        """返回链表长度，时间 O(1)
        """
        return self.size
class LRUCache(object):    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.hashmap = {}
        self.cache = DoubleList()
    
    def makeRecently(self, key):
        """将某个 key 提升为最近使用的
        """
        x = self.hashmap[key]
        self.cache.remove(x)
        self.cache.addLast(x)
    
    def addRecently(self, key, val):
        '''添加最近使用的元素
        '''
        x = Node(key, val)
        #链表尾部就是最近使用的元素
        self.cache.addLast(x)
        self.hashmap[key] = x
        
    def deleteKey(self, key):
        """删除某一个 key
        """
        x= self.hashmap[key]
        self.cache.remove(x)
        self.hashmap.pop(key)
        
    def removeLeastRecently(self):
        """删除最久未使用的元素
        """
        deletedNode = self.cache.removeFirst()
        deletedKey = deletedNode.key 
        self.hashmap.pop(deletedKey)
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashmap:
            return -1
        self.makeRecently(key)
        return self.hashmap[key].val
    
    def put(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap:
            self.deleteKey(key)
            self.addRecently(key, val)
            return
        
        if self.cap == self.cache.size:
            self.removeLeastRecently()
        self.addRecently(key, val)
######################################
## APPROACH 1
# 1. OrderedDict can be used, but won't work in interviews.

## APPROACH 2
# 1. Storing the Double linked Nodes in a Hashmap Works. (key = key, value = Node)
# 2. Head and tail Nodes to start with. (head <==> tail)
# 3. For every get operation, remove the Node, append to tail. (tail will always have last used node)
# 4. For every put operation, append before tail.
# 5. Eviction will be done at head as insertion is done at tail.

## TIME COMPLEXITY : O(1) ##
## SPACE COMPLEXITY : O(N) ##

class DLinkedNode(): 
    def __init__(self,k,v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache1:

    def __init__(self, capacity):
        self.size = capacity
        self.cache = {}
        self.head = DLinkedNode(0, 0)
        self.tail = DLinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        if key in self.cache:
            currNode = self.cache[key]
            self._remove(currNode)
            self._add(currNode)
            return currNode.val
        return -1
        
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        currNode = DLinkedNode(key, value)
        self._add(currNode)                 # add to DLL
        self.cache[key] = currNode          # store value in cache i.e hashmap.
        if len(self.cache) > self.size:     # evict LRU now from both DLL,HM
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
            
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


## ORDERED DICT SOLUTION

from collections import OrderedDict
class LRUCacheeeee:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)      

if __name__ == "__main__":
    unittest.main()