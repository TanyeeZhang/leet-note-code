# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/length-of-last-word/
   Status: Passed
   Performance: 36ms and 13.7MB
"""


class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        """
        :param s: 字符串
        :return:  最后一个单词的长度
        """
        """
        这次摆明了想偷个懒-_-
        """
        s = s.strip()
        return len(s.split(' ')[-1])


print(Solution.lengthOfLastWord('Hello  World'))