# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/7/17
   Description: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
   Status: Passed
   Performance: 48ms and 14.5MB
"""
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        """
        :param prices: 股票价格序列
        :return: 最大利润
        """
        """
        好吧，我承认了，这个题我是看了一下答案= =
        因为暴力法时间超限，双指针法不适用...暂时没招了。可是！
        看了题解，我的天，工作时候还设计过“实时计算动态回撤率”，跟这个方法思路一致啊！
        为什么现在退步这么明显，完了完了...
        """
        length = len(prices)
        min_price = 1 << 31
        max_profit = 0
        for i in range(length):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

    @staticmethod
    def maxProfit_(prices: List[int]) -> int:
        length = len(prices)
        max_profit = 0
        for i in range(length):
            for j in range(i+1, length):
                diff = prices[j] - prices[i]
                max_profit = diff if diff > max_profit else max_profit
        return max_profit


print(Solution.maxProfit([7, 10, 5, 3, 5, 4]))
print(Solution.maxProfit([7, 6, 4, 1]))
print(Solution.maxProfit([2, 1, 4]))
