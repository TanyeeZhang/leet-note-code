# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/plus-one/
   Status: Passed
   Performance: 40ms and 13.7MB
"""
from typing import List


class Solution:
    @staticmethod
    def plusOne(digits: List[int]) -> List[int]:
        """
        :param digits: 表示整数的单个数字的数组
        :return: 加1后的结果
        """
        """
        经过两个用链表表示的整数相加这道题的磨炼后，这个题显得挺easy喔~
        """
        length = len(digits)
        i = 0
        carry = 0
        digits[-1] = digits[-1] + 1
        while i < length:
            if carry:
                digits[-(i + 1)] = digits[-(i + 1)] + carry
                carry = 0
            if digits[-(i + 1)] >= 10:
                digits[-(i + 1)] = digits[-(i + 1)] - 10
                carry = 1
            i += 1
        if carry:
            digits.insert(0, 1)
        return digits


print(Solution.plusOne([9, 9, 9]))
