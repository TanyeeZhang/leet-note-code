# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/8
   Description: https://leetcode-cn.com/problems/maximum-subarray/
   Status: Passed
   Performance: 48ms and 14.4MB
"""
from typing import List


class Solution:
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        """
        :param nums: 整数数组
        :return: 连续子数组的最大和
        """
        """
        刚看到这题时，就纳闷，这是简单题吗？看到题目似乎要求时间复杂度要O(n)...这可难死宝宝了
        因为最简单直接的是双重for循环完事儿~但是好像并不高明，而且可能还会超时！
        我刚开始真是没有思路，想着这咋整？这太难了吧。在纸上画啊画，慢慢发现可能要从“正负”切入。
        我的思路是一边遍历，一边记录此前的最大值，分几种情况讨论：
        1. 当前值大于此前最大值且此前最大值为负，则令最大值为当前值，并将这个值保存下来
        2. 当前值为正且当前值与此前最大值相加为正，则说明和最大子数组要包括该值
        3. 不满足上述条件，说明子数组要“断”了，那么此前最大值要重置了
        最后在这过程中产生的最大值中求出一个最大值。
        一次遍历完成即可得答案。
        不过写得还是很绕的。因为我提交了三次都没过！我都不敢再提交了...反正我这么做很容易错。
        待会看看好的做法，肯定没我这么丑陋~哈哈。
        """
        # if not nums:
        #     return - 1 << 31
        tmp_max = nums[0]
        tmp_arr = [tmp_max]
        for i in range(1, len(nums)):
            if nums[i] > tmp_max and tmp_max < 0:
                tmp_max = nums[i]
                tmp_arr.append(tmp_max)
            elif nums[i] > 0 or tmp_max + nums[i] > 0:
                tmp_max += nums[i]
                tmp_arr.append(tmp_max)
            else:
                tmp_max = 0 if tmp_max > 0 else tmp_max  # 如果此前最大值为负，那就不管它
        # print(tmp_arr)
        return max(tmp_arr)


print(Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution.maxSubArray([-1, 1, -2, 2, -3, 3, 100, 0, 1, 0, 0]))
print(Solution.maxSubArray([-3, 100, -2, 3, -4, 1]))