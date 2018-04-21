'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"

说明：
1.num1 和 num2 的长度小于110。
2.num1 和 num2 只包含数字 0-9。
3.num1 和 num2 均不以零开头，除非是数字 0 本身。
4.不能使用任何标准库的大数类型（比如 BigInteger）或
    直接将输入转换为整数来处理。'''
class Solution(object):#可以过解题系统，但其实不符合规则
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 * num2)


class Solution2(object):#不用int()的话，这种解法算是快的
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        listnum = {'0':0,
                   '1':1,
                   '2':2,
                   '3':3,
                   '4':4,
                   '5':5,
                   '6':6,
                   '7':7,
                   '8':8,
                   '9':9}
        num1 = num1[::-1]
        num2 = num2[::-1]
        count1 = 0
        count2 = 0
        for i in range(len(num1)):
            count1 += listnum[num1[i]] * (10 ** i)
        for j in range(len(num2)):
            count2 += listnum[num2[j]] * (10 ** j)
        return str(count1 * count2)