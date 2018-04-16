'''在未排序的数组中找到第 k 个最大的元素。
请注意，它是数组有序排列后的第 k 个最大元素，
而不是第 k 个不同元素。

例如，
给出 [3,2,1,5,6,4] 和 k = 2，返回 5。

注意事项:

你可以假设 k 总是有效的，1 ≤ k ≤ 数组的长度。'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse = True)#sort逆序的写法，注意一下
        if k>=1 and k <= len(nums):
            return nums[k-1]