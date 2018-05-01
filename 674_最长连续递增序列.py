'''
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:
输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

示例 2:
输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。
'''

class Solution(object):
    #用两个变量记录当前子序列长度和历史子序列最长长度
    #只遍历一遍，最后输出历史以来最长的值就好
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max = 1
        count = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                count += 1
                if count > max:
                    max = count
            else:
                count = 1
        return max