'''
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
'''
class Solution:
    #108ms
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicn ={}
        for i in s:
            if i not in dicn:
                dicn[i] = 1
            else:
                dicn[i] += 1
        dicn = sorted(dicn.items(),key = lambda x : x[1])
        #建立字典，然后按频率排序
        ans = len(s) + 1
        #初值设成界外值
        for i in dicn:
            if i[1] != 1:
                #频数只有两种，只需要管频数为1的
                break
            indexi = s.index(i[0])
            if indexi < ans:
                ans = indexi
                #取最小的那个索引
        if ans < len(s):
            return ans
        else:
            #借助界外值看循环有没有更新了ans，没更新说明该输出-1了
            return -1

class SolutionBetter:
    #48ms
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #这个全程只需要遍历一次字母表
        letters = 'abcdefghijklmnopqrstuvwxyz'
        res = len(s)
        for x in letters:
            lInd = s.find(x)
            if lInd != -1 and lInd == s.rfind(x) and res > lInd:
                #s.find(x) != -1说明x在s中
                #借助lInd = s.find(x)和lInd == s.rfind(x)
                #即该元素第一个出现（find）和最后一次出现（rfind）是在同一处
                #说明频数为1

                #res > lInd更新，寻找最小索引
                res = lInd
        return -1 if len(s) == res else res
        #最后写法十分python