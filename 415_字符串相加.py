'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：
1.num1 和num2 的长度都小于 5100.
2.num1 和num2 都只包含数字 0-9.
3.num1 和num2 都不包含任何前导零。
4.你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''
class Solution(object):#不给用int，那就用字典吧
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        pow = 1
        count1 = 0
        dicn = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        num1 = num1[::-1]
        for i in num1:
            count1 += pow * dicn[i]
            pow *= 10
        pow = 1
        count2 = 0
        num2 = num2[::-1]
        for i in num2:
            count2 += pow * dicn[i]
            pow *= 10
        return str(count1 + count2)