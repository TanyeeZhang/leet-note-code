# coding=utf-8
"""
   Filename: good_solution
   Author:
   Date: 2020/7/17
   Description: https://leetcode-cn.com/problems/climbing-stairs/solution/70zhong-quan-chu-ji-python3hui-ji-liao-ti-jie-qu-w/
"""


class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        """
        这样空间复杂度就是O(1)了
        """
        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a+b
        return b


print(Solution.climbStairs(50))