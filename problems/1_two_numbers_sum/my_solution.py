# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/3/30
   Description: https://leetcode-cn.com/problems/two-sum/
   Status: Passed
   Performance: 924ms and 14.5MB
"""
from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        """
        :param nums: 输入的数组
        :param target: 两数之和
        :return: 两数的索引
        """
        """
        看了别人的解法，感觉自己的脑子好像很笨...（去掉“好像”）
        我的思路是从原数组nums中通过target得到另一个“互补”的队列_nums
        然后遍历_nums，根据我敏（愚）锐（蠢）的洞察力，发现与当前数字“互补”的数字一定在后面所以还用了[i+1:]切片操作
        如果那个数字存在，那么我就把当前的数和索引记下来，这个时候，我还要去查那个数字的索引...再来一次循环...
        哎，说多了都是泪...一只智商不够的^(*￣(oo)￣)^
        """
        _nums = list(map(lambda x: target - x, nums))
        result = []
        candidate = 0
        for i, v in enumerate(_nums):
            if v in nums[i+1:]:
                result.append(i)
                candidate = v
                break
        for k, n in enumerate(nums):
            if n == candidate and k > result[0]:
                result.append(k)
                break
        return result


print(Solution.twoSum([-3, 3, 1, 1, 3, 3], 6))
