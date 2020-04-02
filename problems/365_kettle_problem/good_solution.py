# coding=utf-8
"""
   Filename: kettle
   Author: wangcode
   Date: 2020/3/28
   Description: https://leetcode-cn.com/problems/water-and-jug-problem/solution/
   shui-hu-wen-ti-de-jie-ti-si-kao-java-by-wang-code-/
"""


class Solution:
    @staticmethod
    def canMeasureWater(x: int, y: int, z: int) -> bool:
        """
        深度优先遍历
        经典的解法，加上简洁可行的代码！棒！
        用元组来表示当前状态...Emm不错。切记：遍历的是节点，节点里存的是状态！这个状态的定义要随机应变灵活应用了~
        深度和广度优先遍历区别就是：深度遍历路径是“A”，而广度遍历路径是“Z”...（自创说法...自己懂就行）
        不过这个程序可以适当优化...遍历过程中加入了不必要的节点= =
        """
        stack = [(0, 0)]
        seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False

