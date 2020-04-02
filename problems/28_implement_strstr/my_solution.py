# coding=utf-8
"""
   Filename: my_solution
   Author: Tanyee
   Date: 2020/3/31
   Description:
   Status: Passed
   Performance: 40ms and 13.6MB
"""


class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        """
        :param haystack: 原字符串
        :param needle: 待查字符串
        :return: 是否存在：若存在返回索引；若不存在返回-1；空字符串返回0
        """
        """
        本来还沾沾自喜呢，哈哈，偷鸡的写法，通过！一看评论，这种写法被喷出shi...
        脸红了，无比羞愧...
        人家都在讨论着什么KMP、Sunday算法...听不懂，溜了...
        不配在程序界混T_T
        算了，安慰自己是“实用主义（能实现就行）”，我反正不是为了面试找工作刷题的~啦啦啦~
        （不过知道了还有个find方法，跟index方法差不多，只是后者会报异常，前者会返回-1）
        """
        try:
            index = haystack.index(needle)
        except ValueError:
            index = -1
        return index


print(Solution.strStr('hello', 'll'))
print(Solution.strStr('apple', 'bba'))
print(Solution.strStr('abc', ''))