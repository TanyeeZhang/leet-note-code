# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/3/31
   Description: https://leetcode-cn.com/problems/reverse-integer/
   Status: Passed
   Performance: 40ms and 13.4MB
"""


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        """
        :param x: 32位数字
        :return: 输出反转后的数字
        """
        """
        这道题倒是比较简单，我的思路是“字符串反转拼接”，不过，写得...依旧存在一些瑕疵-_-|||
        1. 一看到反转就想到字符串反转，思维固化！
        2. 2**31可以用位运算啊，是能快一些的...
        3. 适当情况下用三元表达式，看起来简洁（养眼）。
        """
        sign = ''
        if x < 0:
            x = -x
            sign = '-'
        str_x = sign + ''.join(reversed(str(x)))
        res = int(str_x)
        if res > 2**31 - 1 or res < -2**31:
            res = 0
        return res


print(Solution.reverse(-123))
print(Solution.reverse(123))
print(Solution.reverse(-1111111111111111111111))
print(Solution.reverse(120000000))