'''
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

示例 1:
输入: "A"
输出: 1

示例 2:
输入: "AB"
输出: 28

示例 3:
输入: "ZY"
输出: 701
'''


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicn = {'A': 1, 'B': 2, 'C': 3, "D": 4, "E": 5, "F": 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
                'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
        #用ord也行，还快点。但个人习惯上个字典
        sizes = len(s)

        ans = 0

        for i in range(sizes):
            ans += 26 ** (sizes - 1 - i) * dicn[s[i]]
        #结合纸的话很容易搞出推导式，重点在这个-1.
        #对应的168题式子的-1就不容易搞出来
        return ans