# coding=utf-8
"""
   Filename: good_solution
   Author: LeetCode
   Date: 2020/4/13
   Description: https://leetcode-cn.com/problems/string-to-integer-atoi/solution/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/
"""
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        """
        啧啧！有限状态自动机~上学的时候学过，不过不知所云...现在再学一遍~
        根据题意做出以下表格，即可实现。
        S -- (c) --> S' (S状态经过c变为S'状态，这里的c就是字符串中的字符)
        	        ' '	    +/-	     number	   other
        start	    start	signed	in_number	end
        signed	    end	     end	in_number	end
        in_number	end	     end	in_number	end
        end	        end	     end	end	        end
        """
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        return automaton.sign * automaton.ans
