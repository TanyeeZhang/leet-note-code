# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/4/11
   Description: https://leetcode-cn.com/problems/zigzag-conversion/
"""
from pprint import pprint


class Solution:
    @staticmethod
    def convert(s: str, numRows: int) -> str:
        """
        :param s: 字符串
        :param numRows: 给定行数
        :return: 按照正常顺序读取的字符串
        """
        """
        这代码我不会再看第二遍！！！
        晚上跟这题杠上了，睡意全无，从凌晨两三点到凌晨六点。
        越做脑子越乱，但不行，一定要做做做做做做！
        代码写成了一坨XX..
        思路就是放在二维数组里面遍历，提交之后，看了一眼官方解答——
        啊我死了。
        看评论区，貌似像我一样的智障还不少，哈哈哈。
        补觉去了。
        """
        symbol = ''
        if numRows <= 0:
            return ''
        length = len(s)
        if numRows == 1 or numRows >= length:
            return s
        # 计算有多少个组和剩余项（我定义一竖列和一斜列为一组）
        # 在纸上画图即可推导出公式
        # 可以简化下面代码，我头大，反正这代码写得跟啥一样，不看了，不管了
        group, rest = divmod(length, 2 * (numRows - 1))
        if group == 0:
            numCols = length - numRows + 1
        else:
            if rest == 0:
                numCols = group * (numRows - 1)
            else:
                if rest > numRows:
                    numCols = group * (numRows - 1) + rest - numRows + 1
                else:
                    numCols = group * (numRows - 1) + 1
        # print(numRows, numCols)
        m = [[symbol] * numCols for _ in range(numRows)]
        pre = 0
        for j in range(numCols):
            for i in range(numRows):
                # 竖着遍历
                if j % (numRows - 1) == 0 and pre < length:
                    m[i][j] = s[pre]
                    pre += 1
                    # 斜着遍历，是不是惊了...我是被自己蠢笑了
                    if i == numRows-1 and j < numCols-1:
                        i, j = i - 1, j + 1
                        while j % (numRows - 1) != 0 and pre < length:
                            m[i][j] = s[pre]
                            i, j = i - 1, j + 1
                            pre += 1
        # pprint(m)
        _s = ''
        for i in range(numRows):
            for j in range(numCols):
                if m[i][j] != symbol:
                    _s += m[i][j]
        return _s


pprint(Solution.convert('LEETCODEISHIRING', 4))
