# coding=utf-8
"""
   Filename: good_solution
   Author: lucifer
   Date: 2020/4/8
   Description: https://leetcode-cn.com/problems/maximum-subarray/solution/wu-chong-jie-fa-san-chong-yu-yan-java-javascript-2/
"""
from typing import List


class Solution:
    # @staticmethod
    # def maxSubArray(nums: List[int]) -> int:
    #     """
    #     大神之解！
    #     这么看起来，咦，这题难吗= =
    #     """
    #     max_, sum_ = nums[0], nums[0]
    #     for n in nums[1:]:
    #         sum_ = sum_ + n if sum_ >= 0 else n
    #         max_ = max_ if max_ > sum_ else sum_  # 比max快点?
    #     return max_

    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        """
        动态规划！
        大神之解！
        这么看起来，咦，这题难吗= =
        动态规划的难点在于找到状态转移方程：
        dp[i] - 表示到当前位置i的最大子序列和
        状态转移方程为：
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        初始化：dp[0] = nums[0]
        从状态转移方程中，我们只关注前一个状态的值，所以不需要开一个数组记录位置所有子序列和，只需要两个变量。
        """
        n = len(nums)
        curr_index = max_sum = nums[0]
        for i in range(1, n):
            curr_index = max(curr_index + nums[i], nums[i])
            max_sum = max(curr_index, max_sum)
        return max_sum
