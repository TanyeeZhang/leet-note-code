# coding=utf-8
"""
   Filename: good_solution
   Author: jimmy00745
   Date: 2020/3/30
   Description: https://leetcode-cn.com/problems/add-two-numbers/solution/guan-fang-ti-jie-de-python3-c-shi-xian-by-jimmy007/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        """
        官方解法的Python版。
        简洁，漂亮~再看看我的，简直是一坨...我只求能通过，做题效率不高，写得也丑陋...
        这个题的难点在于“进位”的处理，我是被这个搅得一团糟。其实不那么复杂的，我觉得自己过于心急想写出来，没有完全捋顺思路，
        边写边补救哈哈哈哈，一路上坎坎坷坷，缝缝补补，提交通过，执行速度竟然还超过了92.76%的用户...
        还是多膜拜膜拜优秀的代码，切记：思路是第一位的，脑子一定要清楚。绕来绕去，修修补补的时候，这代码基本是没眼睛看的...
        很多时候数据结构都是挂在嘴上，真要实现起来，还真够喝一壶的。一个小小的单链表，就足以让我虚弱...
        """
        dummyHead = ListNode(0)
        curr, carry = dummyHead, 0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10       # 无意中发现，Python内置了divmod方法，e.g divmod(17,4)得到(4,1),元组中前一个是商、后一个是余数
            curr.next = ListNode(sum % 10)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(1)
        return dummyHead.next