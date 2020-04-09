# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/8
   Description: https://leetcode-cn.com/problems/count-and-say/
   Status: Passed
   Performance: 40ms and 13.6MB
"""


class Solution:
    @staticmethod
    def countAndSay(n: int) -> str:
        """
        :param n: 行数
        :return: 对应的数列
        """
        """
        说来也巧，这个题我出过面试题，不过是找规律hhh
        言归正传，这个题嘛，不难，隐隐约约觉得应该可以用递归来做，但是最终没想出来递归怎么做...
        只能来个双重循环搞定。思路很简单，就是判断前一个字符和后一个字符是否相同，然后统计相同字符的个数。
        最后需要注意一下边界的处理。
        """
        if n == 1 or n == 2:
            s = '1' * n
        else:
            s = '11'
            for _ in range(2, n):
                count = 1
                ss = ''
                length = len(s)
                for i in range(1, length):
                    if s[i] == s[i-1]:
                        count += 1
                    else:
                        ss += str(count) + s[i-1]
                        count = 1
                    if i == length-1:
                        ss += str(count) + s[i]
                        count = 1
                s = ss
        return s


print(Solution.countAndSay(9))
print(Solution.countAndSay(10))