'''
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。
键盘自己低头看看电脑。

示例1:
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]

注意:
1.你可以重复使用键盘上同一字符。
2.你可以假设输入的字符串将只包含字母。
'''
class Solution(object):
    #这个用其他方法可能可以快一点，可是要牺牲可读性。所以就这么地吧
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = 'qwertyuiopQWERTYUIOP'
        line2 = 'asdfghjklASDFGHJKL'
        line3 = 'zxcvbnmZXCVBNM'
        ans = []
        for word in words:
            Flag = True
            if word[0] in line1:
                for alpha in word[1:]:
                    if alpha not in line1:
                        Flag = False
                        break
                if Flag:
                    ans.append(word)
            if word[0] in line2:
                for alpha in word[1:]:
                    if alpha not in line2:
                        Flag = False
                        break
                if Flag:
                    ans.append(word)
            if word[0] in line3:
                for alpha in word[1:]:
                    if alpha not in line3:
                        Flag = False
                        break
                if Flag:
                    ans.append(word)
        return ans