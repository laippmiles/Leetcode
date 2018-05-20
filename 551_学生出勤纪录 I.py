'''
给定一个字符串来代表一个学生的出勤纪录，这个纪录仅包含以下三个字符：
'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤纪录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),
那么这个学生会被奖赏。
你需要根据这个学生的出勤纪录判断他是否会被奖赏。

示例 1:
输入: "PPALLP"
输出: True

示例 2:
输入: "PPALLL"
输出: False
'''

class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1:
            return False
        if 'LLL' in s:
            #如果有超过两个超过两个连续的'L'(迟到)
            #那肯定字符串存在LLL
            #只找这个就行
            return False

        return True