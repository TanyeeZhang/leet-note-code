# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/valid-parentheses/
   Status: Passed
   Performance: 36ms and 13.7MB
"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        """
        :param s: 括号表达式
        :return: 是否是正确的表达式
        """
        """
        哈哈，这次几乎和官方思路一样喔~
        因为看到这这个题自然会想到经典的“表达式求值”，当然是用栈啦。
        思路是大概是：按照顺序读取字符串，如果是左括号则入栈，右括号则出栈，出栈时判断是否与当前括号相对应。
        第一次提交没过，因为忘了考虑在pop时栈为空的情形，加上if判断就可以啦~
        """
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if s[i] in mapping.keys():
                if stack:
                    _s = stack.pop()
                    if _s != mapping[s[i]]:
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False


print(Solution.isValid('{([])}'))

