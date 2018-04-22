'''给一个非负整数 num，反复添加所有的数字，直到结果只有一个数字。

例如:
设定 num = 38，过程就像： 3 + 8 = 11, 1 + 1 = 2。 由于 2 只有1个数字，所以返回它。

进阶:
你可以不用任何的循环或者递归算法，在 O(1) 的时间内解决这个问题么？

贡献者:
特别感谢 @jianchao.li.fighter 用于添加此问题并创建所有测试用例。'''

class Solution(object):#60ms
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        nums = str(num)
        while len(nums)>1:
            sums = 0
            for i in nums:
                sums += int(i)
            nums = str(sums)
        return sums


class Solution2(object):#36ms
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        count = 0
        while len(num) != 1:
            for i in num:
                count += int(i)
            num = str(count)
            count = 0

        return int(num)

class SolutionBest(object):#没走循环的解法
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return (num-1) % 9 + 1