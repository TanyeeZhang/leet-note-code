# coding=utf-8
"""
   Filename: good_solution
   Author: liweiwei1419
   Date: 2020/4/10
   Description: https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
"""


class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:
        """
        上动态规划！
        P(i,j) = P(i+1,j-1) and Si == Sj
        用dp[i][j]表示子串s(i,j)是否为回文子串。
        比如“bcacb”是回文串，那么“abcacba”一定是回文串。
        所以动态规划嘛，就是在填一张表格。而且i<=j，只需要填上半部分。
        边界条件是[i+1,j-1]长度小于等于1，则j-1-(i+1)+1<=1，得j-i<=2(或表示为j-i<3)
        """
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]
