'''
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。'''

class Solution(object):#36ms
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        num = str(int(''.join(digits)) + 1)
        digi = []
        for i in num:
            digi.append(int(i))
        return digi

class SolutionBest(object):#26ms
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = ''
        for i in digits:
            tmp += str(i) #善用字符串合并大法
        tmp = int(tmp) + 1
        digits = [int(i) for i in list(str(tmp))]
        return digits