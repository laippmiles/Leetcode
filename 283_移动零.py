'''
给定一个数组 nums，
编写一个函数将所有 0 移动到数组的末尾，
同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''

class Solution(object):
    #简单，可是慢到出翔
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        for i in range(count):
            nums.append(0)

class SolutionBest(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        size = len(nums)
        for idx, num in enumerate(nums):
            if num == 0:
                zeros += 1 #登记0的个数
            else:
                nums[idx - zeros] = num
                #非零元素右移，画图或者结合示例好懂
        for idx in range(zeros):
            nums[size - 1 - idx] = 0
            #写好末尾的0