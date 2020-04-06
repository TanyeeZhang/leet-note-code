# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/4
   Description: https://leetcode-cn.com/problems/longest-common-prefix/submissions/
   Status: Passed
   Performance: 92ms and 13.7MB
"""
from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        """
        :param strs: 字符串数组
        :return: 公共最长前缀
        """
        """
        这次我的解法还是不错的！当然思路也很简单，就是选第一个字符串作为主元，其余的字符串都依次和它比较。
        如果其中某个字符串已经遍历完或者其中有字符不相等，那就跳出并返回。
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        pivot = strs[0]
        leng = len(pivot)
        length = len(strs)
        for i in range(leng):
            for j in range(1, length):
                if i >= len(strs[j]) or strs[j][i] != pivot[i]:
                    return pivot[:i]
        return pivot


print(Solution.longestCommonPrefix(['aaa', 'aa', 'aaa']))