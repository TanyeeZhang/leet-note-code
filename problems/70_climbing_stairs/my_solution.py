# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/7/17
   Description: https://leetcode-cn.com/problems/climbing-stairs/
   Status: Passed
   Performance: 48ms and 13.7MB
"""


class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        """
        :param n: 台阶的数量
        :return: 走法
        """
        """
        喔天啦噜！这个很经典的爬楼梯问题——去年还给同事讲过。
        递归和动态规划两种写法~
        但是我居然很脑残地用了数组！根本没必要啊！
        而且数组初始化让人笑掉大牙...直接[0]*10 就可以了啊！！！还extend，我也是服了我自己...
        """
        # solutions = [0] * 10
        # solutions[0], solution[1] = 1, 2
        solutions = [1, 2]
        solutions.extend([0 for i in range(n-2)])
        for i in range(2, n):
            solutions[i] = solutions[i-1] + solutions[i-2]
        return solutions[n-1]

    @staticmethod
    def climbStairs_(n: int) -> int:
        if n in [1, 2]:
            return n
        else:
            return Solution.climbStairs(n - 1) + Solution.climbStairs(n - 2)


# print(Solution.climbStairs_(50))
print(Solution.climbStairs(5))
