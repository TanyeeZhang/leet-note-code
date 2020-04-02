# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/1
   Description: https://leetcode-cn.com/problems/remove-element/
"""
from typing import List


class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        """
        :param nums: 原数组
        :param val: 目标值
        :return: 不包含目标值的数组长度
        """
        """
        哈哈哈，又来投机取巧啦。真香！
        其实我也感到些许耻辱，想写个正规解法，花了十来分钟没写出来，汗颜...
        不想写了，反正老子通过了，就是这么理直气壮，哼！
        """
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break
        return len(nums)


print(Solution.removeElement([0, 1, 2, 2, 2, 3, 0, 4, 2], 2))