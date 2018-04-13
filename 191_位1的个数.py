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