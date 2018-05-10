'''
给定两个表示复数的字符串。
返回表示它们乘积的字符串。
注意，根据定义 i2 = -1 。

示例 1:
输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

示例 2:
输入: "1+-1i", "1+-1i"
输出: "0+-2i"
解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。

注意:
1.输入字符串不包含额外的空格。
2.输入字符串将以 a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。
输出也应当符合这种形式。
'''
class Solution(object):#按需写作即可
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lista = a[:-1].split('+')
        listb = b[:-1].split('+')
        for i in range(len(lista)):
            lista[i] = int(lista[i])
        for i in range(len(listb)):
            listb[i] = int(listb[i])
        count1 = lista[0]*listb[0] - lista[1]*listb[1]
        count2 = lista[0]*listb[1] + lista[1]*listb[0]
        ans = str(count1) + '+' + str(count2) + 'i'
        return ans