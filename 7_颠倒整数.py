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