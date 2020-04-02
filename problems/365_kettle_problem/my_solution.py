# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/3/28
   Description: https://leetcode-cn.com/problems/water-and-jug-problem/
   Status: Passed
   Performance: 60ms and 13.7MB
"""
from math import gcd


class Solution:
    @staticmethod
    def canMeasureWater(x: int, y: int, z: int) -> bool:
        """
        :param x: X壶的水容量
        :param y: Y壶的水容量
        :param z: 目标Z升水
        :return: 是否能成功
        """
        """
        强行在纸上推导了好久...不知道贝祖定理啊!
        我是分了好多种情况讨论的...心累-_-|||
        虽然通过了，但代码很烂...不想再看第二遍hhh
        不过还是强行记下这个定理吧：（百度百科）
        裴蜀定理（或贝祖定理）得名于法国数学家艾蒂安·裴蜀，说明了对任何整数a、b和它们的最大公约数d，关于未知数x和y的线性不定方程（称为裴蜀等式）：
        若a,b是整数,且gcd(a,b)=d，那么对于任意的整数x,y,ax+by都一定是d的倍数，特别地，一定存在整数x,y，使ax+by=d成立。
        它的一个重要推论是：a,b互质的充要条件是存在整数x,y使ax+by=1.
        """
        if x + y < z or z < 0:
            return False
        if x + y == z or z == 0:
            return True
        if x == 0 and y == 0 and z != 0:
            return False
        if x == 0 and y != 0 and z != 0:
            return True if z % y == 0 else False
        if y == 0 and x != 0 and z != 0:
            return True if z % x == 0 else False
        if z % x == 0 or z % y == 0:
            return True
        if gcd(y, x) * gcd(z, x) == 1:
            return True
        if gcd(y, x) == gcd(z, x) and 1 not in [gcd(y, x), gcd(z, x)]:
            return True
        if gcd(y, x) != gcd(z, x) and 1 not in [gcd(y, x), gcd(z, x)]:
            return False
        if gcd(y, x) == 1 and gcd(z, x) != 1:
            return True
        if gcd(y, x) != 1 and gcd(z, x) == 1:
            return False


print(Solution.canMeasureWater(3, 5, 4))
