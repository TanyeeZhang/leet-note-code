# coding=utf-8
"""
   Filename: good_solution
   Author: jyd
   Date: 2020/6/20
   Description: https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
"""
from typing import List


class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        """
        （以下段落摘抄自评论区）
        其实我们显然可以发现影响问题的两个关键因素，一个是最短的短板，一个是宽度。
        如果宽度变小，那么面积想比之前的更大，唯一的可能是最短的短板比之前要高。
        所以更高的木板根本没必要移动，动它没有任何意义。如果想在更短的宽度得到更大的面积，唯一的可能是移动最短的短板，以期望其变高。短板原理啊，朋友们，是不是刷着刷着题突然就领悟到了人生的哲理。
        所以大家不要老是想这道题该不该用双指针去解；看清这题的本质，自然而然就意识到双指针显然是个较优解。
        """
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
