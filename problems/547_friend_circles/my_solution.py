# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/3/31
   Description: https://leetcode-cn.com/problems/friend-circles/
   Status: Passed
   Performance: 308ms and 13.8MB
"""
from typing import List


class Solution:
    @staticmethod
    def findCircleNum(M: List[List[int]]) -> int:
        """
        这次是知道用深度优先遍历了，但是...还是写得不好。主要是遍历矩阵那儿，我觉得最大的毛病就是我之前总喜欢把东西转换成
        自己顺手的方式，但是这样就可能会影响效率。其实没有必要把矩阵转成字典的...当然我写的时候甚至觉得这很必要= =啊啊啊啊
        还有就是对“图”这一块其实是不大熟的，递归遍历还是要多加理解和运用。划重点！递归！！这很基础啊！！！我的软肋->_<-
        看了解析，知道了“并查集”这个新名词...孤陋寡闻了耶~待会看看。
        """
        """
        :param M: “朋友关系矩阵”
        :return: 朋友圈的个数
        """
        row_map = {}
        N = len(M)
        circles = []  # 保存每个朋友圈的具体成员，这是我做的扩展咯~，原题目不要求，可删去~
        circles_num = 0
        stack = []
        visited = set()  # 注意，{1,2,3}这种声明就代表是set类型了
        for i in range(N):
            row_arr = []
            for j in range(N):
                if M[i][j] == 1 and i != j:
                    row_arr.append(j)
            row_map[i] = row_arr
        for k, v in row_map.items():
            stack.append(k)
            if k not in visited:
                visited.add(k)
                circle_arr = set()
                while stack:
                    # print(visited)
                    circle_arr.add(k)
                    current = stack.pop()
                    tmp_v = row_map.get(current)
                    for i in tmp_v:
                        if i not in visited:
                            stack.append(i)
                            visited.add(i)
                            circle_arr.add(i)
                circles_num += 1
                circles.append(circle_arr)
        # print(circles)
        # print(len(circles))
        return circles_num


# print(Solution.findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
# print(Solution.findCircleNum([[1, 0, 1, 1], [0, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]))
print(Solution.findCircleNum(
    [[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]))
