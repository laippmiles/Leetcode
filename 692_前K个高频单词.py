'''
给一非空的单词列表，返回前 k 个出现次数最多的单词。
返回的答案应该按单词出现频率由高到低排序。
如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：
输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。


示例 2：
输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。


注意：
1.假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
2.输入的单词均由小写字母组成。
'''


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dicn = {}
        for word in words:
            if word not in dicn:
                dicn[word] = 1
            else:
                dicn[word] += 1
        #做哈希表
        dicn = sorted(dicn.items(), key=lambda x: (-x[1], x[0]))
        #重点在key=lambda x: (-x[1], x[0]) 这个排序规则
        #意思是先按-x[1]为规则排序
        #当-x[1]排序规则使两个元素不分先后时按x[0]规则分先后
        ans = [dicn[i][0] for i in range(k)]
        return ans