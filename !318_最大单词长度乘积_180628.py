'''
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，
并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。
如果不存在这样的两个单词，返回 0。

示例 1:
输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "xtfn"。

示例 2:
输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。

示例 3:
输入: ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。
'''

#参考：
#https://www.hrwhisper.me/leetcode-maximum-product-of-word-lengths/

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        nums = [0] * n
        for i, word in enumerate(words):
            for c in word:
                nums[i] |= 1 << (ord(c) - 97)

        #先对word做个预处理
        #比如‘ab’→‘11’(二进制)，说明有a，b两个字母
        #    由       for c in word:
        #        nums[i] |= 1 << (ord(c) - 97)  实现转换
        #这里知道ord（c）输出字母的ascii码，'a'对应的acsii码即可
        #比如b，就会使1左移两位，然后过|=运算即可记录该字符串是否有b这个字母了

        ans = 0
        for i in range(n):
            for j in range(i, n):
                if nums[i] & nums[j] == 0:
                #通过两个字符串间的num相与是否为零判断它们有没有共同字母
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans