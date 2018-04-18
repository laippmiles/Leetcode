'''给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。
如果可以构成，返回 true ；否则返回 false。
=
(题目说明：为了不暴露赎金信字迹，
要从杂志上搜索各个需要的字母，
组成单词来表达意思。)

注意：
你可以假设两个字符串均只含有小写字母。
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true'''
class Solution(object):#132ms
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        listMagazine = []
        for i in magazine:
            listMagazine.append(i)
        for j in ransomNote:
            if j not in listMagazine:
                return False
            else:
                del listMagazine[listMagazine.index(j)]
        return True

class SolutionBest(object):#56ms
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True