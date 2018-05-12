'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
'''
class Solution(object):
    #很直感的看需求写作，其实略慢
    #36ms
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if nums[0] > target:
                return 0
            elif nums[-1] < target:
                return len(nums)
            else:
                for i in range(len(nums) - 1):
                    if target > nums[i] and target < nums[i + 1]:
                        return i + 1


class SolutionBest(object):
    #24ms
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
            #这里没问题
        else:
            #直接把target加到原列表走一波sort，最后直接提取索引反而最快
            #反正python大法注意善用内置函数就对了
            nums.append(target)
            nums.sort()
            return nums.index(target)
