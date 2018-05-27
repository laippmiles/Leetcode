'''
给出一个字符串数组words组成的一本英语词典。
从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。
若其中有多个可行的答案，则返回答案中字典序最小的单词。
若无答案，则返回空字符串。

示例 1:
输入:
words = ["w","wo","wor","worl", "world"]
输出: "world"
解释:
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。

示例 2:
输入:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出: "apple"
解释:
"apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。

注意:
1.所有输入的字符串都只包含小写字母。
2.words数组长度范围为[1,1000]。
3.words[i]的长度范围为[1,30]。
'''
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        initlist = ['']
        wordset = set(initlist)
        #其实可以直接写set([''])，可这样IDE会报错
        ans = ''
        for word in sorted(words):
            if word[:-1] in wordset:
                #这里注意，但字符比如'a'是有'a'[:-1] = ''的
                #[:-1]可理解为取除去最后一个元素
                #所以初始化时要有个''，保证第一个字母能录进词集
                wordset.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans