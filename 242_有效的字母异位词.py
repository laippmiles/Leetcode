'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。
'''
class Solution(object):
    #普通地会用集合就行
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = set(s)
        if S != set(t):
            return False
        for i in S:
            if s.count(i) != t.count(i):
                return False
        return True