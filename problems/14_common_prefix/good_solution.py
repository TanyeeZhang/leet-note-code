# coding=utf-8
"""
   Filename: good_solution
   Author: baiyizhe
   Date: 2020/4/6
   Description: https://leetcode-cn.com/problems/longest-common-prefix/solution/python3-jian-dan-jie-fa-by-baiyizhe/
"""
from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        """
        牛人！
        zip的妙用！我对这个zip方法确实一直用得不是很熟练~以后要记下来咯
        （另外，还有一个令人跪拜的方法：os.path.commonprefix(strs)，一行即可解决！！天啦噜，不活了...）
        """
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s