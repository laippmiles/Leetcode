'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

例如，
给定数组 [1,1,1,2,2,3] , 和 k = 2，返回 [1,2]。

注意：
1.你可以假设给定的 k 总是合理的，1 ≤ k ≤ 数组中不相同的元素的个数。
2.你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        #字典大法
        #利用sorted + lambda 对字典排序
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dicn = {}
        for i in nums:
            if i not in dicn:
                dicn[i] = 1
            else:
                dicn[i] += 1
        #print(dicn)
        dicn = sorted(dicn.items(), key=lambda e:e[1], reverse=True)
        #关于sorted + lambda 的用法:https://www.cnblogs.com/hf8051/p/8085424.html
        #key=lambda e:e[1]
        #key = ：排序标准
        #lambda e:e[1]：e指sorted里头处理对象的一个元素，e[1]指按第二个元素排序
        #print(dicn)
        #顺带一提，字典没有sort，只有sorted排序，会生成一个元素为元组的列表
        ans = []
        for i in range(k):
            ans.append(dicn[i][0])
        return ans

#a = Solution()
#a.topKFrequent([4,1,-1,2,-1,2,3] , 2)