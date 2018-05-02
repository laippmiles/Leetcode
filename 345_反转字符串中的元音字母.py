'''
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：
给定 s = "hello", 返回 "holle".
示例 2：
给定 s = "leetcode", 返回 "leotcede".

注意:
元音字母不包括 "y".
'''
class Solution(object):#慢到惨绝人寰的方法
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = list(s)
        ans1 = []
        yuanyin = 'aeiouAEIOU'
        for i in s:
            if i in yuanyin:
                ans1.append(i)
        ans1 = ans1[::-1]
        index = 0
        for j in range(len(ans)):
            if ans[j] in yuanyin:
                ans[j] = ans1[index]
                index += 1
        strans = ''
        for k in ans:
            strans = strans + k

        return strans

    class SolutionBest(object):#只用遍历一次的方法
        def reverseVowels(self, s):
            """
            :type s: str
            :rtype: str
            """
            vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
            l = list(s)
            i = 0
            j = len(l) - 1
            while i < j:
                while i < j and l[i] not in vowels:
                    i += 1
                while i < j and l[j] not in vowels:
                    j -= 1

                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1

            return ''.join(l)
