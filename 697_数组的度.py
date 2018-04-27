'''
给定一个非空且只包含非负数的整数数组 nums,
数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:
输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2:
输入: [1,2,2,3,1,4,2]
输出: 6

注意:
nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。

'''

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicn = {}
        for i in range(len(nums)):
            if nums[i] not in dicn:
                dicn[nums[i]] = []
                dicn[nums[i]].append(i)
            else:
                dicn[nums[i]].append(i)
                #用字典保存每种元素对应的索引，而且是有序列表
        count = 0
        ans = 0
        for j in dicn:
            if len(dicn[j]) > count:
                #找出频数最多的元素，字典对应值列表两端的索引差+1即为需要输出的答案
                count = len(dicn[j])
                ans = (dicn[j][-1] - dicn[j][0] + 1)
            elif len(dicn[j]) == count:
                #有时有些元素频数一样，选较小的ans输出
                if (dicn[j][-1] - dicn[j][0] + 1) < ans:
                    ans = (dicn[j][-1] - dicn[j][0] + 1)
        return ans