# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/longest-palindromic-substring/
   Status: Passed
   Performance: 7820ms and 14.6MB
"""


class Solution:
    @staticmethod
    def _palindrome(s: str) -> str:
        pivot = s[-1]
        for i in range(len(s) - 1):
            if s[i] == pivot and s[i:] == ''.join(reversed(s[i:])):
                return s[i:]
        return ''

    @staticmethod
    def _max(s1: str, s2: str) -> str:
        return s1 if len(s1) > len(s2) else s2

    @staticmethod
    def longestPalindrome(s: str) -> str:
        """
        :param s: 字符串
        :return: 最长回文子串
        """
        """
        居然提交一次就通过了！虽然写得不好，但还是挺受鼓舞的！
        
        """
        if len(s) <= 1:
            return s
        return Solution._max(Solution.longestPalindrome(s[:len(s) - 1]), Solution._palindrome(s[:len(s)]))


print(Solution.longestPalindrome('xyzabcdcbammmnmm'))