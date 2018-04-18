'''给定一个字符串，找到它的第一个不重复的字符，
并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。'''
class Solution(object):#200ms
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sets = []#保存已经排除的字母
        for i in s:
            if i not in sets and s.count(i) == 1:
                return s.index(i)
            if i not in sets:
                sets.append(i)
        return -1


class SolutionBest(object):#42ms
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        minIdx = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            #只用查询26遍，这是这个范例最核心的trick了
            curIdx = s.find(c)
            if curIdx != -1 and curIdx == s.rfind(c):
                #s.find(c) != -1表示find在字符串找到了c
                #find() 是从字符串左边开始查询子字符串匹配到的第一个索引
                #rfind()是从字符串右边开始查询字符串匹配到的第一个索引
                #s.find(c) == s.rfind(c)表示无论从左还是从右找
                # c被找到的位置都一样，这说明字符串里只有一个c
                minIdx = min(minIdx, curIdx)
                #替换目前找到的最小值，代表第一个（最靠左）的索引
        return minIdx if minIdx != len(s) else -1