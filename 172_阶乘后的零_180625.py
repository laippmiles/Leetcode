'''
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

示例 2:
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.

说明: 你算法的时间复杂度应为 O(log n) 。
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #参考这个
        #https://blog.csdn.net/NoMasp/article/details/50568854
        #遇见5的倍数会多一个0
        count = 0
        while n > 0:
            a = n / 5
            count += a
            n = a
        return count