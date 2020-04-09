# coding=utf-8
"""
   Filename: good_solution
   Author: xilepeng
   Date: 2020/4/9
   Description: 
"""
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        """
        思路和我一样，只是写得更精简一些。不过还是要学习哒~
        """
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
