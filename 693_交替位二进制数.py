'''给定一个正整数，检查他是否为交替位二进制数：
换句话说，就是他的二进制数相邻的两个位数永不相等。

示例 1:
输入: 5
输出: True
解释:5的二进制数是: 101

示例 2:
输入: 7
输出: False
解释:7的二进制数是: 111

示例 3:
输入: 11
输出: False
解释:11的二进制数是: 1011

示例 4:
输入: 10
输出: True
解释:10的二进制数是: 1010
'''
class Solution(object):#暴力法效果就挺好的了
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = bin(n)[2:]
        for i in range(len(num)-1):
            if num[i] == num [i+1]:
                return False
        return True