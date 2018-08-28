class Solution(object):  # 40ms:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = self.searchFirst(nums, target, 0, len(nums) - 1)
        r = self.searchLast(nums, target, 0, len(nums) - 1)
        return [l, r]

    def searchFirst(self, nums, target, begin, end):
        if begin > end:
            return -1
        mid = (begin + end) // 2
        if nums[mid] == target:
            if (mid > 0 and nums[mid - 1] != target) or mid == 0:
                #注意寻找的条件
                return mid
            else:
                end = mid - 1
        elif nums[mid] < target:
            begin = mid + 1
        else:
            end = mid - 1
        return self.searchFirst(nums, target, begin, end)
        #用递归找第一个待找数的索引

    def searchLast(self, nums, target, begin, end):
        if begin > end:
            return -1
        mid = (begin + end) // 2
        if nums[mid] == target:
            if (mid < len(nums) - 1 and nums[mid + 1] != target) or mid == len(nums) - 1:
                return mid
            else:
                begin = mid + 1
        elif nums[mid] < target:
            begin = mid + 1
        else:
            end = mid - 1
        return self.searchLast(nums, target, begin, end)