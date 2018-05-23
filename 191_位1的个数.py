'''
编写一个函数，输入是一个无符号整数，
返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

示例 :
输入: 11
输出: 3
解释: 整数 11 的二进制表示为 00000000000000000000000000001011

示例 2:
输入: 128
输出: 1
解释: 整数 128 的二进制表示为 00000000000000000000000010000000
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        strn = bin(n)[2:]
        listn = []
        for i in strn:
            listn.append(i)
        return listn.count('1')

class Solution1(object):#其实不用改列表
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        strn = bin(n)[2:]
        count = 0
        for i in strn:
            if i == '1':
                count += 1
        return count

class SolutionBest(object):#利用位移和逻辑运算的，难理解一点，可是快挺多
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = 0
        while n > 0:
            if n & 1 == 1:
                counts += 1
            n >>= 1 #右位移
        return counts