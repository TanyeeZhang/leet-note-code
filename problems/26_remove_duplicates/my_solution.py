# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
   Status: Passed
   Performance: 68ms and 14.8MB
"""
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        """
        :param nums: 排好序的数组
        :return: 不含重复元素的新数组的长度
        """
        """
        因为之前先做了第27题，所以这个第26题就不费功夫了。
        这题的关键点是：把数（按照顺序）往前挪。
        """
        count = 1
        length = len(nums)
        if length <= 1:
            return length
        for i in range(1, length):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        # print(nums)
        return count


print(Solution.removeDuplicates([-1, 0, 1, 1, 2, 3, 3, 3, 4, 4, 5]))
