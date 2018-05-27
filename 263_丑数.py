'''
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。
'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in [2,3,5]:
            while num % i == 0:
                num = num/i#对2,3,5这三个因数除到尽为止
        if num == 1:
            return True
        else:
            return False