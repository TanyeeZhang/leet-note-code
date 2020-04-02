# coding=utf-8
"""
   Filename: good_solution
   Author: leicj
   Date: 2020/4/1
   Description: https://leetcode-cn.com/problems/remove-element/solution/python3-yi-chu-yuan-su-by-leicj/
"""
from typing import List


class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        """
        把与目标值不相等的元素往前扔...我当初想的是往后挪，最后，仔细读题，发现，这题emm没意思...<_<
        """
        # i为不同元素的数组的长度
        i = 0
        for j in range(0, len(nums)):
            # 如果nums[j]不等于val, 则将nums[j]赋值给nums[i]即可, i自增
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i