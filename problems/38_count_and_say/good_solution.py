# coding=utf-8
"""
   Filename: good_solution
   Author: liu-wan-lao-da-ye
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/count-and-say/solution/di-gui-qiu-jie-by-liu-wan-lao-da-ye/
"""


class Solution:
    @staticmethod
    def countAndSay(n: int) -> str:
        """
        咦，递归还能这么用？！受教了，受教了！
        此题用递归解的基础是：countAndSay(n)处理的是countAndSay(n-1)的结果。
        主要步骤如下：
        如果n=1，返回字符串'1'
        得到countAndSay(n-1)的字符串， 从字符串的第一位开始处理，辅助一个计数值count_num：表示重复的字符数，以及num：前一位的字符
        如果当前位与前一位一样，那么count_num加1；
        如果当前位于前一位不一样，那么需要把前面的字符输出，即追加 count_num+num的字符串；
        最后，为了保证最后一位的信息也添加进去，增加了一步：strs += count_num + char的操作。
        最后，返回字符串strs即可。
        """
        if n == 1:
            return '1'
        count_num = 0
        num = ''
        strs = ''
        char = ''
        for char in Solution.countAndSay(n-1):
            if char != num:
                if count_num > 0:
                    strs += str(count_num) + num
                count_num = 1
                num = char
            else:
                count_num += 1
        strs += str(count_num) + char
        return strs
