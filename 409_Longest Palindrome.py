'''
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicn = {}
        for i in s:
            #建立字典，统计每个字母的出现频率
            if i not in dicn:
                dicn[i] = 1
            else:
                dicn[i] += 1

        dicn = sorted(dicn.items(), key=lambda x: x[1], reverse=True)
        #字典排序
        jishu = 0
        count = 0
        for j in dicn:
            if j[1] % 2 == 1 and jishu != 0:
                #出现频数为奇数，但在奇数频数中不是最多的字母
                #去掉一个以后加入回文组
                count += j[1] - 1
                continue
            if j[1] % 2 == 1 and jishu == 0:
                #出现频数为奇数，且在奇数频数中是最多的字母
                #加入回文组
                count += j[1]
                jishu = 1
            elif j[1] % 2 == 0:
                #出现频数为偶数的字母，加入回文组
                count += j[1]
        return count