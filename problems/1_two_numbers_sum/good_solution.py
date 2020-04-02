# coding=utf-8
"""
   Filename: good_solution
   Author: laolarouyuejiaoyuexiang
   Date: 2020/3/30
   Description: https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/
"""
from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        """
        hashmap存储前面遍历过的数字的值和索引
        遍历nums过程中，看target-num是否之前出现过
        """
        """
        把查过的数字存在字典里，我居然没想到T_T
        """
        hashmap = {}
        for i, num in enumerate(nums):
            candidate = hashmap.get(target - num)
            if candidate is not None:
                return [candidate, i]
            hashmap[num] = i

