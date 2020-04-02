# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/1
   Description: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
   Status: Passed
   Performance: 40ms and 13.4MB
"""


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """
        :param s: 原字符串
        :return: 最长不含重复字符的字符串长度
        """
        """
        这次思想跟“主流”思想（滑动窗口）大体一致，只是不该用find方法的...又留下了污点@_@
        其实不用find的，每次有重复字符进入的时候移动一下i，否则一直移动j。
        下次要记住啦，用好[i, j)这对好基友~
        P.S. 还附上了动态规划的解法~当然是看到了marcusxu讲解的启发，稍有改动。
        关键的点还是在于状态转移方程： L(s) = max(L(s-1), find_left(s))
        """
        str_s = ''
        length = 0
        i = 0
        res = 0
        while i < len(s):
            index = str_s.find(s[i])
            str_s += s[i]
            if index != -1:
                str_s = str_s[index+1:i+1]
                length = len(str_s)
            else:
                length += 1
            if length > res:  # 可以用max啦，不过也可以不用
                res = length
            # print(s[i], '->', str_s) 从中可以看到最长字符串的变化
            i += 1
        return res

    # @staticmethod
    # def L(s: str) -> int:
    #     """
    #     思想源泉：
    #     https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/
    #     python3ti-jie-chao-jian-dan-de-dong-tai-gui-hua-ji/
    #     """
    #     if s == '':
    #         return 0
    #     if len(s) == 1:
    #         return 1
    #
    #     def find_left(s_):  # 从末尾一路向左找
    #         tmp_str = ''
    #         j = len(s_) - 1
    #         while j >= 0 and s_[j] not in tmp_str:
    #             tmp_str += s_[j]
    #             j -= 1
    #         return len(tmp_str)
    #
    #     return max(Solution.L(s[:-1]), find_left(s))


print(Solution.lengthOfLongestSubstring('aabbxyz'))