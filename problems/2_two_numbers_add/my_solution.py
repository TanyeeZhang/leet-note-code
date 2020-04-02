# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/3/30
   Description: https://leetcode-cn.com/problems/add-two-numbers/
   Status: Passed
   Performance: 64ms and 13.6MB
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def visit(self):
        current = self
        while current is not None:
            print(current.val, end='')
            current = current.next
        print()

    def __add__(self, other):
        return Solution.addTwoNumbers(self, other)


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        """
        :param l1: 链表1
        :param l2: 链表2
        :return: 相加后的链表
        """
        """
        数字用链表的形式相加，上大学的时候《数据结构》考试的最后一道题就是这个= =当时只是用文字和伪代码描述了算法过程。
        今天写起来，感觉还是踩了一些坑...而且看了大神们的解答...再次感觉自己现在coding能力实属堪忧T_T
        代码里面存在冗余，懒得改了，感觉思维还是不够精炼！拖泥带水...绕来绕去的，写起来容易错，看起来也不是很容易理解吧。
        还是需要再提高Fighting~
        关于解题的过程其实没什么可说...思路大体没问题，进位那里，我投机取巧了，两个整数相加，进位就是1，不过确实需要
        更严谨一些的。
        """
        current1 = l1
        current2 = l2
        res = ListNode(0)
        origin = res
        delta = 0
        while True:
            res.val = current1.val + current2.val + delta
            delta = 0
            if res.val >= 10:
                res.val = res.val - 10
                delta = 1
            current1 = current1.next
            current2 = current2.next
            if current1 is None and current2 is None:
                if delta != 0:
                    res.next = ListNode(1)
                break
            if current1 is None and current2 is not None:
                if delta != 0:
                    _current = current2
                    while current2 is not None:
                        current2.val = current2.val + delta
                        if current2.val >= 10:
                            current2.val -= 10
                            delta = 1
                        else:
                            delta = 0
                        if current2.next is None:
                            if delta != 0:
                                current2.next = ListNode(1)
                                break
                        current2 = current2.next
                    res.next = _current
                else:
                    res.next = current2
                break
            if current2 is None and current1 is not None:
                if delta != 0:
                    _current = current1
                    while current1 is not None:
                        current1.val = current1.val + delta
                        if current1.val >= 10:
                            current1.val -= 10
                            delta = 1
                        else:
                            delta = 0
                        if current1.next is None:
                            if delta != 0:
                                current1.next = ListNode(1)
                                break
                        current1 = current1.next
                    res.next = _current
                else:
                    res.next = current1
                break
            res.next = ListNode(0)
            res = res.next
        return origin


node1 = ListNode(9)
node1.next = ListNode(9)
node1.next.next = ListNode(9)
node1.visit()

node2 = ListNode(9)
node2.next = ListNode(9)
node2.next.next = ListNode(9)
node2.next.next.next = ListNode(9)
node2.next.next.next.next = ListNode(9)
node2.visit()

(node2 + node1).visit()
