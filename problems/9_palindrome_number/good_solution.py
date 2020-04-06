# coding=utf-8
"""
   Filename: good_solution
   Author: MisterBooo
   Date: 2020/4/3
   Description: https://leetcode-cn.com/problems/palindrome-number/solution/dong-hua-hui-wen-shu-de-san-chong-jie-fa-fa-jie-ch/
"""


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        """
        官方解法的Python版本（代码不长，我自己改写的）
        具体做法如下：
        1. 每次进行取余操作（ %10），取出最低的数字 y = x % 10
        2. 将最低的数字加到取出数的末尾：revertNum = revertNum * 10 + y
        3. 每取一个最低位数字，x 都要自除以 10
        4. 判断 x 是不是小于 revertNum ，当它小于的时候，说明数字已经对半或者过半了
        5. 最后，判断奇偶数情况：如果是偶数的话，revertNum 和 x 相等；如果是奇数的话，最中间的数字就在revertNum 的最低位上，将它除以 10 以后应该和 x 相等。
        核心思想就是：取出后半段数字进行翻转。
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10
