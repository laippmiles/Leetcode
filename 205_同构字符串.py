'''给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换最终变成 t ，则两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。
两个字符不能映射到同一个字符上，但字符可以映射自己本身。

例如，
给定 "egg", "add", 返回 true.
给定 "foo", "bar", 返回 false.
给定 "paper", "title", 返回 true.'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        lists = []
        listt = []
        for i in range(len(s)):
            lists.append(s[i])
            listt.append(t[i])
        return  len(set(zip(lists,listt))) == len(set(lists)) == len(set(listt))
        #其实没必要转成列表,字符串本身是可迭代对象就可以zip了

class SolutionBest(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return  len(set(zip(s,t))) == len(set(s)) == len(set(t))#写成这样就行啦