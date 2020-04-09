# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/sqrtx/
   Status: Passed
   Performance: 3264ms and 13.6MB
"""


class Solution:
    @staticmethod
    def mySqrt(x: int) -> int:
        """
        :param x: 非负整数
        :return: 平方根
        """
        """
        程序执行耗时真！的！长！
        我的思路有点傻= =
        先不断地除2，直到平方小于原数（为啥这么做？啊，为了加速啊= =）
        然后又转向愚蠢地循环，嘿嘿嘿。我是小（大）天（笨）才（蛋）！
        """
        if x <= 1:
            return x
        res = x
        while res * res > x:
            res = res >> 1
        for i in range(res, x):
            if (i + 1) ** 2 > x:
                return i


print(Solution.mySqrt(10000000000000))
