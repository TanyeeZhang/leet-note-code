# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/7
   Description: https://leetcode-cn.com/problems/search-insert-position/
   Status: Passed
   Performance: 40ms and 14.4MB
"""
from typing import List


class Solution:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        """
        :param nums: 有序数组
        :param target: 目标值
        :return: 若存在，返回索引；若不存在，返回插入位置
        """
        """
        徒手写的递归二分查找...当然这个不是很难啦~
        主要是判断begin(left)和end(right)边界的时候很容易错。
        P.S.现在不投机取巧了，不用import bisect的方法了哈哈哈，思想觉悟提高了喔~
        """
        def bisect(_nums: List[int], _target, begin=0, end=0) -> int:
            if begin >= end and _target != _nums[begin]:
                return begin if _nums[begin] > _target else begin + 1
            mid = (begin + end) // 2
            if _nums[mid] == _target:
                return mid
            elif _nums[mid] > _target:
                return bisect(_nums, _target, 0, mid - 1)
            else:
                return bisect(_nums, _target, mid + 1, end)
        return bisect(nums, target, 0, len(nums)-1)


print(Solution.searchInsert([1, 2, 3, 4], 10))
