'''
给定一个字符串数组，将字母异位词组合在一起。
字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
1.所有输入均为小写字母。
2.不考虑答案输出的顺序。
'''

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        alps = strs.copy()
        for i in range(len(alps)):
            alps[i] = tuple(sorted([alp for alp in alps[i]]))
            #可以更改数值的都不能做字典的键
            #所以要改成排序后的元祖

        dicn = {}

        for j in range(len(alps)):
            if alps[j] not in dicn:
                dicn[alps[j]] = []
                dicn[alps[j]].append(j)
            else:
                dicn[alps[j]].append(j)
        ans = []

        for k in dicn:
            ans.append([strs[i] for i in dicn[k]])

        return ans


class Solution2:
    #另一种字典大法，运算速度好像挺看脸的。
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicn = {}
        for s in strs:
            key = list(s)
            #直接list一个字符串会得到由其字母组成元素的列表
            #例：list('asd')→['a', 's', 'd']
            key.sort()
            #过一次排序
            key = ''.join(key)
            #组合成字符串，要不没法做字典的键

            #上面三行可以组合成
            # key = ''.join(sorted(list(s)))
            if key not in dicn:
                dicn[key] = []
                dicn[key].append(s)
            else:
                dicn[key].append(s)

        return list(dicn.values())