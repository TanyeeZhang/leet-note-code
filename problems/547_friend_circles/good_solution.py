# coding=utf-8
"""
   Filename: good_solution
   Author: PrinnyW
   Date: 2020/3/31
   Description: https://leetcode-cn.com/problems/friend-circles/solution/xie-de-mei-guan-yi-dian-de-bing-cha-ji-by-prinnyw/
"""


class Solution:
    @staticmethod
    def findCircleNum(M) -> int:
        """
        哇~领略了“并查集”大法，醍醐灌顶。
        贴一篇博客：https://blog.csdn.net/liujian20150808/article/details/50848646，关于并查集，讲得生动形象，诙谐幽默。
        大体分为find-union两步走：
        find，找“祖先”，也就是找到组织的“老大”；
        union，为了“联谊”使“老大”屈服...
        并查集主要用在元素的划分问题上。
        （代码中注释是我加的。）
        """
        father = [i for i in range(len(M))]  # 刚开始，每个人都是自己的老大

        def find(a):
            if father[a] != a:
                father[a] = find(father[a])  # 一直找上级组织，找到老大为止，在这里继续敲黑板！要熟练掌握递归...当然用while也可。
            return father[a]

        def union(a, b):
            father[find(b)] = find(a)  # 为了联谊，自己的老大认别人的老大为老大<_<
            return find(b)

        for i in range(len(M)):   # 根据题意，开始操作（因为是对称矩阵，搞一半儿就可以了）
            for j in range(i):
                if M[i][j]:
                    union(i, j)

        for i in range(len(M)):  # 咳咳，重新梳理一下老祖宗，这下不少人祖先重复了，用set过滤一下^_^
            find(i)

        return len(set(father))
