'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
'''
class Solution(object):
    #不算快，胜在直观
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ''
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        pre = ''
        for i in range(len(strs[0])):
            pre += strs[0][i]
            for j in range(len(strs)):
                if strs[j][:i+1] != pre:
                    return ans
            ans = pre
        return ans

class SolutionBest(object):
    #这个用了zip
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        r = ''
        for letters in zip(*strs):
            #关于zip(）参考：
            #http://www.runoob.com/python/python-func-zip.html
            #zip() 函数用于将可迭代的对象作为参数，
            #将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
            #如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
            # 利用 * 号操作符，可以将元组解压为列表。
            #示例：
            #zip(*[(1, 4), (2, 5), (3, 6)]) 会返回一个可迭代的zip对象
            #list化以后可以看到里面内容是[(1, 2, 3), (4, 5, 6)]
            com_prefix = set(letters)
            if len(com_prefix) != 1:
                return r
            r += com_prefix.pop()
            #com_prefix是集合，不能通过索引得到元素
            #所以用pop（）获取头元素（反正也就一个元素）
        return r