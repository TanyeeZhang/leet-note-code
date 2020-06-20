# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/6/19
   Description: https://leetcode-cn.com/problems/container-with-most-water/
"""
from typing import List
#
#
# class Solution:
#     @staticmethod
#     def area(line1, line2):
#         return min(line1[1], line2[1]) * (line2[0]-line1[0])
#
#     @staticmethod
#     def maxArea(height: List[int]) -> int:
#         length = len(height)
#         arr = []
#         max_area = 0
#         current_bound = None
#         for index, value in enumerate(height):
#             arr.append((index, value))
#
#         index = 0
#         for i in arr:
#             index += 1
#             if index < length:
#                 for j in arr[index:]:
#                     area = Solution.area(i, j)
#                     if area > max_area:
#                         max_area = area
#         return max_area


class Solution:
    """
    上面是用暴力法写的，果然，时间超限...
    这个是时隔一天之后，我灵光突现，用了“双指针”，挺巧妙的~
    """
    @staticmethod
    def area(height, left, right):
        return min(height[left], height[right]) * (right-left)

    @staticmethod
    def maxArea(height: List[int]) -> int:
        """
        :param height: 组成容器的隔板高度列表
        :return: 容器的最大容量
        """
        length = len(height)
        max_area = 0
        left = 0
        right = length-1
        while left < right:
            area = Solution.area(height, left, right)
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


print(Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution.maxArea([2, 3, 4, 5, 18, 17, 6]))
print(Solution.maxArea([1, 2, 3, 4, 5, 6, 7, 8, 2]))


# ===================================================================================
# 某位小朋友问我的一道题T_T我不知道做的对不对...应该也是leetcode上的题，不过我不知道是哪一道。
# 题的大意是给定一个字符串(如“leetcode”),输出不存在相同字符的子串长度数组。(如[1,7])
# 我的思路是：得到每个字符出现的索引，用有序字典存储；然后循环遍历，判断边界，来合并区间或者独立划分出来(这一块写得不太好懂= =)
# from collections import OrderedDict
#
#
# class Solution:
#     @staticmethod
#     def maxSubstringArr(string: str) -> [int]:
#         hashmap = OrderedDict()
#         index = 0
#         for s in string:
#             if s in hashmap:
#                 hashmap[s].append(index)
#             else:
#                 hashmap[s] = [index]
#             index += 1
#         current_index = (-1, -1)
#         arr = []
#         # print(hashmap)
#         for values in hashmap.values():
#             # print(values, current_index)
#             if len(values) == 1:
#                 if values[-1] > current_index[1]:
#                     arr.append(1)
#                     current_index = (values[0], values[-1])
#             else:
#                 if values[0] < current_index[1] < values[-1]:
#                     arr.append(arr.pop() + values[-1] - current_index[1])
#                     current_index = (current_index[0], values[-1])
#                 elif values[0] > current_index[1]:
#                     arr.append(values[-1] - values[0] + 1)
#                     current_index = (values[0], values[-1])
#         return arr
#
#
# print(Solution.maxSubstringArr('田慧慧我爱你'))
# print(Solution.maxSubstringArr('leetcodc'))
# print(Solution.maxSubstringArr('aaaaaaaabtxyza'))
# print(Solution.maxSubstringArr('babyiloveyou'))
# print(Solution.maxSubstringArr('wIki'))
# print(Solution.maxSubstringArr('ijddacfafh'))
# ==================================================================================