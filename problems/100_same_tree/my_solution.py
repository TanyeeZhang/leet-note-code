# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/same-tree/
   Status: Passed
   Performance: 56ms and 13.6MB
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        """
        :param p: 二叉树p
        :param q: 二叉树q
        :return: 是否相等
        """
        """
        比较简单的一道题，上学的时候就会...
        递归比较左右子树即可。
        """
        if p and q \
                and p.val == q.val \
                and Solution.isSameTree(p.left, q.left) \
                and Solution.isSameTree(p.right, q.right):
            return True
        return False if p != q else True
