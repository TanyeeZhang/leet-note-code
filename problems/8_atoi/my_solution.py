# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/12
   Description: https://leetcode-cn.com/problems/string-to-integer-atoi/
   Status: Passed
   Performance: 48ms and 13.8MB
"""


class Solution:
    number_mapping = {}
    for i in range(10):
        number_mapping[str(i)] = i
    sign_set = ['+', '-']

    @staticmethod
    def convert(s: str) -> int:
        negative_flag = False
        m = 0
        i = 1
        _i = 0
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            return Solution.number_mapping[s[0]] if s[0] in Solution.number_mapping else 0
        if length > 1 and s[0] == '-':
            negative_flag = True
        for _s in s[::-1]:
            _i += 1

            if _s not in Solution.number_mapping and _i < length:
                return 0
            else:
                if _s in Solution.number_mapping:
                    n = Solution.number_mapping[_s]
                    m += n * i
                    i *= 10
        return -m if negative_flag else m

    @staticmethod
    def myAtoi(s: str) -> int:
        """
        :param s: 字符串
        :return: 数字
        """
        """
        有一种越写越差的feel...
        虽然通过各种if/else的“夹击”做出来了~但是，没有任何技术含量...
        思路嘛，也不过就是最浅陋的方式...
        在评论区看到这种写法评价是“基本功不扎实”...确实，深以为然。
        还有，字符串转数字过程中乘法加法要注意溢出的情况。
        """
        left = - 1 << 31
        right = (1 << 31)-1
        res = ''
        s = s.strip()
        if s == '':
            return 0
        if len(s) > 1:
            if s[0] != '+' and s[0] != '-' and Solution.number_mapping.get(s[0]) is None:
                return 0
            for i in s[1:]:
                if i in Solution.number_mapping:
                    res += i
                else:
                    break
            res = s[0] + res
        else:
            res = s
        res = Solution.convert(res)
        if res < left:
            return left
        if res > right:
            return right
        return res


print(Solution.myAtoi('  -123ab 123 '))