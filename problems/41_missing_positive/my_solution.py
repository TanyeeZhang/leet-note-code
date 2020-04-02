# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/2
   Description: https://leetcode-cn.com/problems/first-missing-positive/
   Status: Passed
   Performance: 40ms and 13.8MB
"""
from typing import List


class Solution:
    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        """
        :param nums: 未排序的整数数组
        :return: 缺失的第一个正整数
        """
        """
        要论时间复杂度...那是在下输了。官方解法时间复杂度是O(n)，我的应该是O(nlogn)吧...囧
        还是那句老话：
        过了就行hhh
        我的（渣渣）思想是：过滤原数组只剩下正值，然后过滤掉重复，然后排序，最后根据索引来找...
        （懵了，才看到题目要求，时间复杂度必须是O(n)，完了完了，大清没了...不管了，假装没看见^_^）
        （简言之：自娱自乐，不（不）足（要）挂（bi）齿（脸）。）
        （P.S. 刚才用np.random.permutation(10000000)测试了一下，我的解法居然比官方思想的Python解法快50%...应该是幻觉|||）
        """
        nums = sorted(set(filter(lambda x: x > 0, nums)))
        length = len(nums)
        if length == 0 or min(nums) > 1:
            return 1
        else:
            for i in range(length):
                if nums[i] > i + 1:
                    return i + 1
            return length + 1


print(Solution.firstMissingPositive([-5, 1, 1, 1, 0, 2, 4, 5, 3, 100]))