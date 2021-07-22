# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        lruCache = LRUCache(1)
        self.assertEqual(lruCache.getValueFromKey("a"), None)
        # lruCache.insertKeyValuePair("b", 2)
        lruCache.insertKeyValuePair("a", 1)
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        lruCache.insertKeyValuePair("a", 9001)
        self.assertEqual(lruCache.getValueFromKey("a"), 9001)
        lruCache.insertKeyValuePair("b", 2)
        self.assertEqual(lruCache.getValueFromKey("a"), None)
        self.assertEqual(lruCache.getValueFromKey("b"), 2)
        lruCache.insertKeyValuePair("c", 3)
        self.assertEqual(lruCache.getValueFromKey("a"), None)
        self.assertEqual(lruCache.getValueFromKey("b"), None)
        self.assertEqual(lruCache.getValueFromKey("c"), 3)
        # self.assertEqual(lruCache.getValueFromKey("b"), 2)
        # self.assertEqual(lruCache.getMostRecentKey(), "c")
        # self.assertEqual(lruCache.getValueFromKey("a"), 1)
        # self.assertEqual(lruCache.getMostRecentKey(), "a")
        # lruCache.insertKeyValuePair("d", 4)
        # self.assertEqual(lruCache.getValueFromKey("b"), None)
        # lruCache.insertKeyValuePair("a", 5)
        self.assertEqual(lruCache.getValueFromKey(("a"),5))



class Node:
    def __init__(self,val,key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.map = {}
        self.head = None
        self.tail = None
        self.len =0

    def insertKeyValuePair(self, key, value):
        node = ""
        if self.getValueFromKey(key) is not None:
            node = self.map.get(key)
            node.val = value
        else:
            node= Node(value,key)
        if self.len == self.maxSize:
            self.map.pop(self.tail.key)
            self.tail = self.tail.prev
            self.len -= 1
        self.map[key] = node
        self.len += 1
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        elif self.len == self.maxSize and self.maxSize == 1:
            self.head = node
            self.tail = node
        elif self.head == self.tail and self.head is not None:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def getValueFromKey(self, key):
        if self.map.get(key) is None:
            return None
        else:
            if self.map.get(key) == self.head:
                return self.map.get(key).val
            node = self.map[key]
            if self.tail is not None and self.tail.key == key:
                if self.tail != self.head:
                    self.tail = self.tail.prev
                    self.tail.next = None
            if self.head != node:
                node.prev.next=node.next
            if node.next is not None:
                node.next.prev = node.prev
            node.next = self.head
            if self.head is not None:
                self.head.prev = node
            node.prev = None
            self.head =node
            return self.map.get(key).val


    def getMostRecentKey(self):
        return self.head.key


