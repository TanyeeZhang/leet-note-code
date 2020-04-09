# coding=utf-8
"""
   Filename: good_solution
   Author: powcai
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/plus-one/solution/jian-dan-de-fang-fa-by-powcai/
"""
from typing import List


class Solution:
    @staticmethod
    def plusOne(digits: List[int]) -> List[int]:
        """
        思路基本一致，就是人家写得更好= =
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry, b = divmod(digits[i] + carry, 10)
            digits[i] = b
        if carry:
            digits.insert(0, 1)
        return digits
