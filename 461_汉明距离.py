#两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#给出两个整数 x 和 y，计算它们之间的汉明距离。
#注意：
#0 ≤ x, y < 231.

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ac = bin(x ^ y)
        print(ac)
        count = 0
        for i in ac:
            if i == '1':
                count += 1
        return count

class SolutionBest:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = bin(x ^ y).count("1")
        #直接上count，熟悉列表常用那几个函数
        return r

s =Solution()
print(s.hammingDistance(1,4))