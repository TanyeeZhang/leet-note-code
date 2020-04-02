# coding=utf-8
"""
   Filename: good_solution
   Author: gaussic
   Date: 2020/4/1
   Description: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/comments/2558
"""


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """
        神仙做法！以下解释是从评论区扒下来的：
        i是截至j，以j为最后一个元素的最长不重复子串的起始位置，即索引范围是[i,j]的子串是以索引j为最后一个元素的最长子串。
        当索引从j-1增加到j时，原来的子串[i,j-1]新增了一个元素变为[i,j]，需要判断j是否与[i,j-1]中元素有重复。
        所以if s[j] in st:是判断s[j]相同元素上次出现的位置，和i孰大孰小。
        如果i大，说明[i,j-1]中没有与s[j]相同的元素，起始位置仍取i；
        如果i小，则在[i,j-1]中有了与s[j]相同的元素，所以起始位置变为st[s[j]]+1，即[st[sj]+1,j]。
        而省略掉的else部分，由于s[j]是第一次出现所以前面必然没有重复的，仍然用i作为起始位置即可。
        后面的ans=max(ans,j-i+1)中，括号中前者ans是前j-1个元素最长子串长度，j-i+1是以s[j]结尾的最长子串长度，
        两者（最长子串要么不包括j，要么包括j）取最大即可更新ans，遍历所有i后得到整个输入的最长子串长度。
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans