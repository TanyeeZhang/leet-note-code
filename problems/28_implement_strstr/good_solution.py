# coding=utf-8
"""
   Filename: good_solution
   Author: Tes
   Date: 2020/3/31
   Description: https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/
"""


class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        """
        好像叫Sunday算法，还没仔细研究。后面有时间和KMP一起研究研究吧。
        先挂几个KMP的链接：
        https://haihongblog.com/archives/911.html （翻看了这个作者别的博客，还蛮正能量的...）
        http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html（大名鼎鼎的阮一峰）
        """
        # Func: 计算偏移表
        def calShiftMat(st):
            dic_ = {}
            for i in range(len(st) - 1, -1, -1):
                if not dic_.get(st[i]):
                    dic_[st[i]] = len(st) - i
            dic_["ot"] = len(st) + 1
            return dic_

        # 其他情况判断
        if len(needle) > len(haystack): return -1
        if needle == "":
            return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx + len(needle) <= len(haystack):

            # 待匹配字符串
            str_cut = haystack[idx:idx + len(needle)]

            # 判断是否匹配
            if str_cut == needle:
                return idx
            else:
                # 边界处理
                if idx + len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx + len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]

        return -1 if idx + len(needle) >= len(haystack) else idx
