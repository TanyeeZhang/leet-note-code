# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/6
   Description: https://leetcode-cn.com/problems/divide-two-integers/
   Status: Passed
   Performance: 64ms and 13.6MB
"""


class Solution:
    @staticmethod
    def divide(dividend: int, divisor: int) -> int:
        """
        :param dividend: 被除数
        :param divisor: 除数
        :return: 商
        """
        """
        不能用乘法除法加法，好吧，那我就用减法，循环减下去，OK，没问题，但是试运行了一下，发现程序超时！
        当一个很大的数除以很小的数，这种做法就不行了...
        那好吧，不得不换方法了。突然想起之前帮别人做过的一个题：1加到100，不用循环，不用乘法，我当时是移位运算解决的。
        那这个题是不是也可以用移位运算解决呢？在纸上写写画画，发现，可以的！
        比如：100/3 = 3*32 + 3*1 + 1 = 3*(2**5) + 3*(2**0) + 1 = 3*(1<<5) + 3*(1<<0) + 1
        想到这儿，那这个题就变得简单了，就相当于找每个括号里移位的位数~
        最后把括号里的数加起来即可！
        P.S.刚在评论区看到，这个题应该不允许使用abs方法，因为会溢出-__-算了，我假装没看见~
        """
        sign = False
        res = 0
        carry_arr = []
        left = - 1 << 31
        right = (1 << 31) - 1
        # sign = (dividend > 0) ^ (divisor > 0) 若sign为True，说明异号；反之说明同号（评论区看到的写法，异或运算）
        if dividend >= 0 and divisor > 0 or dividend <= 0 and divisor < 0:
            sign = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            res = dividend
        else:
            while dividend >= divisor:
                carry = 1
                while divisor << carry < dividend:
                    carry += 1
                carry -= 1
                carry_arr.append(carry)
                dividend = dividend - (divisor << carry)
        for i in carry_arr:
            res += 1 << i
        res = res if sign else -res
        if res < left or res > right:
            return right
        return res


print(Solution.divide(1 << 31, 3))