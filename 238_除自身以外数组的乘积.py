'''
给定长度为 n 的整数数组 nums，其中 n > 1，
返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:
输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
'''
class Solution(object):
    #这道题重点在不能用除法
    #核心思想在保存第i个位置之前所有数的乘积和第i个位置之后所有数的乘积
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]
        right = [1]
        for i in range(len(nums)-1):
            left.append(left[i]*nums[i])
            right.append(right[i]*nums[-i-1])
        return[left[j]*right[-j-1] for j in range(len(nums))]