#给定一个字符串，
# 你需要反转字符串中每个单词的字符顺序，
# 同时仍保留空格和单词的初始顺序。
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"

class Solution(object):#最直感，但是很不python的写法
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lists = s.split(' ')
        listre = []
        for word in lists :
            listre.append(word[::-1])
        sre = (' ').join(listre)
        return sre

class SolutionBest(object):#很python风格的写法，而且运行速度比上面那个快（实际思路是一样的）
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return (' ').join(word[::-1] for word in s.split(' '))