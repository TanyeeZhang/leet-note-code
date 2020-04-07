# coding=utf-8
"""
   Filename: good_solution
   Author: wu_yan_zu
   Date: 2020/4/7
   Description: https://leetcode-cn.com/problems/search-insert-position/solution/er-fen-cha-zhao-bian-jie-jie-shi-qing-song-zhang-w/
"""
from typing import List


class Solution:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        """
        二分查找的循环（非递归）写法
        ...其实更容易理解~
        """
        if not nums:
            return 0
        n = len(nums)
        left = 0
        right = n - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        res = left
        return res

