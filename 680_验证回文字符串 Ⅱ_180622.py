'''

给定一个非空字符串 s，最多删除一个字符。
判断是否能成为回文字符串。

示例 1:
输入: "aba"
输出: True

示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。

注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
'''


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPalindrome(s):
            #先写一个判断回文，这个因为s只含小写字母所以好写
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return left, right
                    #在第一个不构成回文的地方记下左右索引
                left += 1
                right -= 1
            return True, True

        left, right = isPalindrome(s)
        if left == True and right == True:
            return True
        else:
            #试着去左边索引的元素看看构不构成回文
            s1 = s[:left] + s[left + 1:]
            left1, right1 = isPalindrome(s1)
            if left1 == True and right1 == True:
                return True
            #左边不行的话，试着去右边索引的元素看看构不构成回文
            s2 = s[:right] + s[right + 1:]
            left2, right2 = isPalindrome(s2)
            if left2 == True and right2 == True:
                return True
            #都不行就真不行了，输出False
            return False