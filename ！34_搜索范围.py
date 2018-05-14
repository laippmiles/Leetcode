'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''
class Solution(object):#40ms:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        listn = []
        for i in range(len(nums)):
            if nums[i] == target:
                listn.append(i)
            if nums[i] > target:
                break
        if len(listn) == 0:
            return [-1,-1]
        else:
            return [listn[0],listn[-1]]


class SolutionBetter(object):#36ms
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        if target not in nums:
            return [-1, -1]
        else:
            left = nums.index(target)
        #确定左象限
        ansl = left
        ansr = left
        #逐步迭代，找到右象限
        while left < n:
            if nums[left] == target:
                ansr = left
                left += 1
            else:
                break
        return [ansl, ansr]
