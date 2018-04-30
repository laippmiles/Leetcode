class Solution(object):#212ms
    #这个方法需要遍历长字符串
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        count = 0
        target = s[count]
        for i in t:
            target = s[count]
            if i == target:
                count += 1
            if count == len(s):
                return True
        if count == len(s):
            return True
        else:
            return False

class SolutionBest(object):#52ms
    #这个方法只需要遍历一遍短字符串
    #利用了字符串的find方法
    #find会返回字符串里待查询的某字符所在索引，如果没找到，函数返回-1
    #参考：http://www.runoob.com/python/att-string-find.html
        def isSubsequence(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            if len(s) == 0:
                return True
            for i in s:
                pos = t.find(i)
                if pos == -1:
                    return False
                else:
                    t = t[pos + 1:]
            return True