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
        我是从第3题那儿获得的灵感：
        状态转移方程如下：
        L(s) = max(L(s-1), palindrome(L(s)))
        其中palindrome(L(s))表示“末尾固定的最长回文子串”
        例如：“dabcba”将末尾的“a”固定住，意思就是要找的最长子串如果不是出现在前面的字符串中，
        那一定包含末尾，那这个题就变简单了：
        依次遍历，看当前字符是否和末尾字符相同，如果相同则直接截取反转判断是否相等（这是我偷懒的做法）
        如果不相同则遍历下一个。
        我觉得这个思路比评论区很多思路理解起来要简单吧= =但程序运行耗时确实长...
        """
        if len(s) <= 1:
            return s
        return Solution._max(Solution.longestPalindrome(s[:len(s) - 1]), Solution._palindrome(s[:len(s)]))


print(Solution.longestPalindrome('xyzabcdcbammmnmm'))