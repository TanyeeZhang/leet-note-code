# coding=utf-8
"""
   Filename: good_solution
   Author: jyd
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        """
        思想跟我一样。只是人家写得真简洁~寥寥数笔，不拖泥带水。我还需打磨啊~~
        P.S.不过这个解法好像没考虑空格的情况= =不过无伤大雅，加个判断语句即可。
        """
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1
