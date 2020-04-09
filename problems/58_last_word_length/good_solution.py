# coding=utf-8
"""
   Filename: good_solution
   Author: dian-shi-ju-2
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/length-of-last-word/solution/x-by-dian-shi-ju-2-2/
"""


class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        """
        这次我偷懒啦。看看别人的做法，其实思路什么的并不难，老老实实循环、老老实实判断空格什么的。
        """
        if not s:
            return 0
        count = 0
        flag = 0
        for i in s[::-1]:
            if i is " " and flag == 0:
                continue
            if i is not " ":
                count += 1
                flag = 1
            else:
                break
        return count