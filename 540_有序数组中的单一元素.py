'''
给定一个只包含整数的有序数组，每个元素都会出现两次，
唯有一个数只会出现一次，找出这个数。

示例 1:
输入: [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。
'''

class Solution(object):
    #注意数组是有序的，只看奇数索引上的第一个跳变就能找出答案啦
    #while的条件注意一下，防溢出
    #最后补一句，防止答案在数组最后（循环扫不到那里）
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2
        return nums[-1]