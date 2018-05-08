'''
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。
返回出现次数最多，同时不在禁用列表中的单词。
题目保证至少有一个词不在禁用列表中，而且答案唯一。

禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。
答案都是小写字母。

示例:
输入:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
输出: "ball"

解释:
"hit" 出现了3次，但它是一个禁用的单词。
"ball" 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。
注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 "ball,"），
"hit"不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
说明:
1.1 <= 段落长度 <= 1000.
2.1 <= 禁用单词个数 <= 100.
3.1 <= 禁用单词长度 <= 10.
4.答案是唯一的, 且都是小写字母 (即使在 paragraph 里是大写的，即使是一些特定的名词，答案都是小写的。)
5.paragraph 只包含字母、空格和下列标点符号!?',;.
6.paragraph 里单词之间都由空格隔开。
7.不存在没有连字符或者带有连字符的单词。
8.单词里只包含字母，不会出现省略号或者其他标点符号。
'''

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        word_alpha_list = [[l.lower() for l in p if l.isalpha()] for p in paragraph.split(' ')]
        #重点在这一句二重推导式
        #参考：
        #https://leetcode.com/problems/most-common-word/discuss/124128/Easy-python-solution
        #去掉标点后，每个词分开，按单个字母保存，如：“ball”→[‘b’,'a','l','l']
        word_list = [''.join(word) for word in word_alpha_list]
        dicn = {}
        for i in word_list:
            if i not in dicn:
                dicn[i] = 1
            else:
                dicn[i] += 1
        dicn = sorted(dicn.items() ,key = lambda x:x[1] ,reverse = True)
        for j in dicn:
            if j[0] not in banned:
                return j[0]