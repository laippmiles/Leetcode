'''
给定一个整数数组 nums ，
找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        #用一个辅助列表保存每到每个元素时的子序和
        a = nums[0]
        ans.append(a)
        for i in range(1,len(nums)):
            if a < 0:
                #如果上一个记载的子序和小于0，则重置成当前元素
                a = nums[i]
                ans.append(a)
            else:
                a += nums[i]
                ans.append(a)
        return max(ans)