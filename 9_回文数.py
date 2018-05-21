'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''
class Solution:#最普通的解法
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]

class Solution2:
    #不给用str()的话...暂时能想到的就拿列表保存每一位数字了╮(╯▽╰)╭
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reverse_num = 0
        count = 0
        s = x
        anslist = []
        ans = 0
        while x > 0:
            tep = x % 10
            x = x // 10
            anslist.append(tep)
        for i in anslist[::-1]:
            ans += i * (10**count)
            count += 1
        return ans == s