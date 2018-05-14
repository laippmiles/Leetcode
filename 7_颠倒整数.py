'''
给定一个 32 位有符号整数，将整数中的数字进行反转。
示例 1:
输入: 123
输出: 321

 示例 2:
输入: -123
输出: -321

示例 3：
输入: 120
输出: 21

注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
根据这个假设，如果反转后的整数溢出，则返回 0。
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import sys
        strx = str(x)
        if x < 0 :
            strx = strx[1:]
        if x > 2**31 or x < -2**31:
            #在整型中说XX位都指2的XX次方（按二进制算的位数）
            #在python中次方是**或者pow，别写成^
            #^表示的是异或，异或计算规则为:（同为0，异为1）
            return 0
        strx = strx[::-1]
        re = int(strx)
        if re > 2**31 :
            return 0
        elif x < 0 :
            return re * -1
        else:
            return re

class SolutionBest:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            x = int(str(x)[::-1])
            if x > pow(2,31):
                #溢出检查
                return 0
            else:
                return x
        else:
            x = -int((str(-x)[::-1]))
            if x < - pow(2,31):
                return 0
            else:
                return x
a = Solution()
print(a.reverse(123))