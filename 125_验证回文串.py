'''
给定一个字符串，验证它是否是回文串，
只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:#两边往中间扫
            if not s[left].isalnum():
                #isalnum:判断字符串是否只有数字字母
                left += 1
                continue
                #扫到标点符号就索引移一位，跳出这次循环了
                #重点是记得要跳，自己写的时候没跳结果代码不工作
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                #记得都转小写
                return False
            left += 1
            right -= 1
        return True