# coding=utf-8
"""
   Filename: good_solution
   Author: boywithacoin_cn
   Date: 2020/3/31
   Description: https://leetcode-cn.com/problems/reverse-integer/solution/pythondan-chu-he-tui-ru-shu-zi-yi-chu-qian-jin-xin/
"""


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        """
        好的代码就是精炼，反观我的代码里丑陋的‘-’负号字符拼接...不说了...
        这个代码中是先取绝对值，然后过程中就不考虑负号的问题了，最后再通过x的正负来决定返回值的正负
        该代码亮点：
        1. 位运算
        2. 用商和余数来得到反转
        3. 三元表达式...（总是忘记用）
        """
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res
