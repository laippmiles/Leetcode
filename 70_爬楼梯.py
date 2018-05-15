'''
假设你正在爬楼梯。需要 n 步你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 步 + 1 步
2.  2 步

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 步 + 1 步 + 1 步
2.  1 步 + 2 步
3.  2 步 + 1 步
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 这道题实际上是斐波那契数列的应用
        #斐波那契数列详见剑指P74-76的解释
        if n <= 2:
            return n
        fnMin1 = 2
        fnMin2 = 1
        ans = 0 #这句话随意的，可是不写IDE会提醒
        #从3开始走循环，用两个变量保存f（n-1）和f（n-2）
        for i in range(3, n + 1):
            ans = fnMin1 + fnMin2
            #更新f（n-1）和f（n-2）
            fnMin2 = fnMin1
            fnMin1 = ans

        return ans