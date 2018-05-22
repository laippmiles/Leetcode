'''

给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:
输入: "Hello World"
输出: 5
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:#防空字符串
            return 0
        lists = [i for i in s.split(' ') if (i != '')]#来个推导式play
        if len(lists) == 0:#防原字符串只有空格
            return 0
        return len(lists[-1])