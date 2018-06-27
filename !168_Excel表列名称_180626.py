'''
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

示例 1:
输入: 1
输出: "A"

示例 2:
输入: 28
输出: "AB"

示例 3:
输入: 701
输出: "ZY"
'''


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dicn = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: "H", 9: 'I', 10: "J", 11: 'K', 12: 'L',
                13: 'M', 14: 'N', 15: 'O',
                16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 0: 'Z'}

        ans = ''

        while n > 0:
            ans += dicn[n % 26]
            n = (n - 1) / 26
            #有点接近26进制的转换，但是不完全相同，注意这个-1
            #参考：
            #https://www.cnblogs.com/lightwindy/p/8606855.html
        return ans[::-1]