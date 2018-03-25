class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        a = word.upper()#所有字母大写
        b = word.lower()#所有字母小写
        c = b.capitalize()#首字母大写
        if word == a or word == b:
            return word == a or word == b
        else:
            return word == c
        #逻辑理清很简单，主要是记得upper，lower，capitalize这三个标准函数