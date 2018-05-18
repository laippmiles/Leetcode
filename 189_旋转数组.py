'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:
1.尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
2.要求使用空间复杂度为 O(1) 的原地算法。

'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k != 0:
            wid = len(nums)
            while k > wid:
                k -= wid #这里注意读题，很多容易出来的
            nums[:] = nums[wid- k:] + nums[:wid- k]
            #重写nums的时候不能直接写nums，要写nums[：]
            #要不好像传不出去，输出仍是原数组