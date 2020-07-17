# coding=utf-8
"""
   Filename: good_solution
   Author: jiang-zhe-hu-di-yi-nuan-nan
   Date: 2020/7/17
   Description: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/python3-dong-tai-gui-hua-zhu-xing-jie-shi-ban-by-j/
"""
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        """
        （1）思路：动态规划
                买卖股票的实质就是：每个元素后面的最大值和当前元素的差，作为该元素为买点的最大利润，那么最佳时机就是这个
            差的最大值。
                以dp数组记录每个元素右边出现的最大值，即dp[i]代表第 i 元素的右边最大值。那么dp[i-1]和dp[i]存在如下关系：
            dp[i] = max(prices[i+1], dp[i+1])，从而最大利润则为max(dp[i]-prices[i])
        （2）复杂度：
            - 时间复杂度：O（n）
            - 空间复杂度：O（n） 当然，不用dp数组储存直接用常量储存也行，复杂度变为O(1)
        """
        # 记录股票价格数组的长度
        ary_len = len(prices)
        # 记录最大利润
        max_num = 0
        # 初始化dp数组并赋初值，为了保证dp[i]刚好代表第i元素后面的最大值，所以pirces数组增加长度1，且置为0
        dp = [0] * ary_len
        prices = prices + [0]
        # 遍历数组补充dp数组的其他值
        for i in range(ary_len-2, -1, -1):
            # 如果prices[i+1] > dp[i+1]，说明prices[i+1] > max(prices[i+1:ary_len])，则dp[i]=prices[i+1]
            if prices[i+1] > dp[i+1]:
                dp[i] = prices[i+1]
            else:
                dp[i] = dp[i+1]
            # 计算以i元素为买入点的最大利润
            if dp[i] - prices[i] > max_num:
                max_num = dp[i] - prices[i]
        return max_num


print(Solution.maxProfit([7, 1, 5, 3, 6, 4]))