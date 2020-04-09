# coding=utf-8
"""
   Filename: good_solution
   Author: yu-fa-tang-you-dian-tian
   Date: 2020/4/9
   Description: https://leetcode-cn.com/problems/same-tree/solution/python-shen-du-bian-li-dfs-di-gui-shi-xian-by-yu-f/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    @staticmethod
    def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        """
        本题关键点在于选定条件
        1.p存在，q不存在，返回False
        2.p不存在,q不存在，返回False
        3.p和q都为None的时候，返回True
        4.除了上述条件下，值相等的情况下进行递归
        （最后用all优化了一下）
        """
        # 看评论有人用type(p)和type(q)进行比较，应该也可以，更简洁一些。
        if p and not q:
            return False
        if not p and q:
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False
        return all((Solution.isSameTree(p.left, q.left),
                    Solution.isSameTree(p.right, q.right)))
