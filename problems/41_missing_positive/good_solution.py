# coding=utf-8
"""
   Filename: good_solution
   Author: haofengsiji
   Date: 2020/4/2
   Description: https://leetcode-cn.com/problems/first-missing-positive/solution/guan-jie-pythongeng-jian-ji-by-haofengsiji/
"""
from typing import List


class Solution:
    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        """
        这是比官方解法更简洁的写法。
        反正这思想真是“绝”...太厉害了啦><
        确实，有时候要将数组的索引和值（之间的关系）用到“极致”。
        有时间要学习Bitmap的思想并实现简单的demo~
        """
        # 保证有1
        if 1 not in nums:
            return 1

        n = len(nums)

        # 保证都在1~n的范围内
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # 以自身正负为bitmap，标记
        for i in range(n):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]

        # 找到第一个为正的索引，即没有出现的最小正数
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # 全为负
        return n + 1
