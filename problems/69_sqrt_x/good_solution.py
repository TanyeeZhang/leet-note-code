# coding=utf-8
"""
   Filename: good_solution
   Author: LeetCode
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode/
"""


class Solution:
    @staticmethod
    def mySqrt(x):
        """
        牛顿迭代法！
        啊啊啊，怎么能没想到！！！
        求x的平方根，即迭代“X(k+1) = (X(k) + x/X(k))/2”即可。
        这道题还有一种递归做法：
        mySqrt(x) = 2 * mySqrt(x/4)
        即：mySqrt(x) = mySqrt(x>>2)<<1
        核心代码如下：
        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        return left if right * right > x else right
        妙绝！
        """
        if x < 2:
            return x
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2
        return int(x1)
