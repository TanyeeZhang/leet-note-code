# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/2
   Description: https://leetcode-cn.com/problems/palindrome-number/submissions/
   Status: Passed
   Performance: 92ms and 13.7MB
"""


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        """
        :param x: 整数
        :return: 是否为回文数
        """
        """
        这次没用“reversed”（应该不会被喷了吧），嘿嘿。
        用了双指针~头指针往后，尾指针往前，直到相遇...
        """
        x = str(x)
        i, j = 0, len(x) - 1
        while i <= j:
            if x[i] == x[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


print(Solution.isPalindrome(12321))