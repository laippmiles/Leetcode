'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。

示例 2:
输入: "aba"
输出: False

示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
'''
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sizes = len(s)
        if sizes == 1:
            return False
        if s == s[0]*sizes:
            return True
        #上面两个是特殊情况，单独写个判断比较好
        i = 2
        ans = s[:i]
        #接下来就是看图说话了，但是这个方法其实挺笨的
        while i <= (sizes/2):
            if sizes % i != 0:
                i += 1
                ans = s[:i]
            else:
                tep = sizes/i
                if s == (ans * tep):
                    return True
                i += 1
                ans = s[:i]
        return False

class SolutionBest(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return s
        #空串另算
        ss=(s+s)[1:-1]
        return ss.find(s)!=-1
        #如果串是重复子字符串的话，那么原串*2掐头去尾的话里面一定包含一个原串
        #用个示例写下来对一下就好理解了