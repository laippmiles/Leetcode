'''
编写一个算法来判断一个数是不是“快乐数”。
一个“快乐数”定义为：对于一个正整数，
每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
如果可以变为 1，那么这个数就是快乐数。

示例:
输入: 19
输出: true
解释:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        setn = set()
        # 用一个集合收集所有遍历过的数字
        # 如果数字发现在即集合里已经有的话，那就说明开始鬼打墙了，False输出吧
        while n not in setn:
            setn.add(n)
            count = 0
            while n > 0:
                count += (n%10)**2
                n /= 10
            if count == 1:
                return True
            n = count
        return False

