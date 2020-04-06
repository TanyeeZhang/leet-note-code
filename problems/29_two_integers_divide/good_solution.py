# coding=utf-8
"""
   Filename: good_solution
   Author: bu-jue-jian-yi-bei-mi-huo
   Date: 2020/4/6
   Description: https://leetcode-cn.com/problems/divide-two-integers/solution/
                29-liang-shu-xiang-chu-by-bu-jue-jian-yi-bei-mi-hu/
"""


class Solution:
    @staticmethod
    def opp(x):
        # 取相反数函数，避免使用‘-’，也算乘法
        # 取反加一，相当于求相反数
        return ~x + 1

    @staticmethod
    def divide(dividend: int, divisor: int) -> int:
        """
        没有溢出！也没有位运算！！
        除数不断加倍，其实暗含着幂运算（移位）
        这才是精髓~之所在。
        """
        res = 1  # 记录结果(无符号)
        sign = 1  # 表示结果正负性（符号）
        # 如果dividend和divisor只有一个大于零，则sign为负；否则为正
        if dividend > 0:
            dividend = Solution.opp(dividend)
            sign = Solution.opp(sign)
        if divisor > 0:
            divisor = Solution.opp(divisor)
            sign = Solution.opp(sign)

        a, b = dividend, divisor
        # 如果除数小于被除数，则结果肯定为0.（注意此时两者都是负数）
        if b < a:
            return 0
        # 通过减法循环，计算除法结果
        a = a - b  # 先计算一次，对应res=1的初始值
        while a <= b:  # 循环过程中不断增加除数的值，减少循环次数，避免超时
            res += res
            b += b
            a -= b
        # 循环结束后，可能存在未处理完的情况，比如 10 - 1 = 9，9 - 2 = 7，7 - 4 = 3，3 - 8 = -5 < 1
        # 它就走出了 while 循环，但是 3 本来还可以减 3 次 1，所以只要再递归
        res = res + Solution.divide(dividend - b, divisor)

        # 处理可能的溢出情况
        if res == 2 ** 31:
            if sign == 1:
                return 2 ** 31 - 1
            else:
                return -2 ** 31
        # 根据sign调整结果的正负性
        else:
            if sign == 1:
                return res
            else:
                return Solution.opp(res)
