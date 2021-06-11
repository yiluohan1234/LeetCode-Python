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
460. LFU Cache
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

 

Example 1:
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3
 

Constraints:

0 <= capacity, key, value <= 104
At most 105 calls will be made to get and put.
'''
import unittest
import collections 
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.k2v = collections.defaultdict(int) # key to value mapping
        self.f2ks = collections.defaultdict(dict) # frequency to keys mapping, noticed each frequency put keys into a map instead of a list. This makes sure we can search a key in O(1)
        self.k2f = collections.defaultdict(int) # key to frequency mapping 
        self.keys = set()  # all keys currently in cache
        self.cap = capacity
        self.lf = 0 # least frequency

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keys:
            return -1
        self.add_freq(key)
        return self.k2v[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        size = len(self.keys)
        if key in self.keys:
            self.k2v[key] = value
            self.add_freq(key)
            return
        
        if size == self.cap:
            self.remove_lfk()
        
        if len(self.keys) < self.cap:
            self.k2v[key] = value
            self.k2f[key] = 1
            self.lf = 1
            self.f2ks[1][key] = 'placeholder'
            self.keys.add(key)
            
            
    def remove_lfk(self):
        if not list(self.f2ks[self.lf].keys()):
            return
        lfk = list(self.f2ks[self.lf].keys())[0]
        self.f2ks[self.lf].pop(lfk)
        if not self.f2ks[self.lf]:
            del self.f2ks[self.lf]
            self.lf+=1
        self.keys.remove(lfk)
        del self.k2v[lfk]
        del self.k2f[lfk]
    
    
    def add_freq(self, key):
        orginal_freq = self.k2f[key]
        self.k2f[key]+=1
        del self.f2ks[orginal_freq][key]
        self.f2ks[orginal_freq+1][key] = 'placeholder'
        if not self.f2ks[self.lf]:
            self.lf+=1
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        
class LFUCache1:

    def __init__(self, capacity):
        self.capacity = capacity
        ## k2v[k]=v : key = k, v = node
        self.k2v = dict() 
        ## f2k[f][k]=v : frequency = f, key = k, v = value 
        self.f2k = collections.defaultdict(collections.OrderedDict)
        ## current least frequenct f2k
        self.LF = 0

    def get(self, key) :
        if key not in self.k2v: 
            return -1
        node = self.k2v[key]
        ## update the frequency
        self.update(node, node.val)
        return node.val
        
    def put(self, key, value):
        if self.capacity == 0: return
        if key not in self.k2v: 
            if len(self.k2v) >= self.capacity:
                ## pop the node with current least freuenct f2k (FIFO)
                k, v = self.f2k[self.LF].popitem(last=False)
                self.k2v.pop(k)
            node = ListNode(key, value)
            ## save the new node into k2v and f2k map
            self.k2v[key] = node
            self.f2k[1][key] = value
            ## reset current LF to 1
            self.LF = 1
        else: 
            ## update the vaLue of existing key 
            node = self.k2v[key]
            node.val = value
            ## update the frequency
            self.update(node, value)
            
            
    def update(self, node, newVal):
        k, f = node.key, node.freq
        ## delete from the former frequency (f)
        self.f2k[f].pop(k)
        ## if the former frequency is the LFU and it become empty
        ## the new frequency (f+1) become new LFU
        if not self.f2k[f] and self.LF == f:
            self.LF += 1
        ## push to the new frequency (f+1)
        self.f2k[f+1][k] = newVal
        node.freq += 1
        

if __name__ == "__main__":
    unittest.main()