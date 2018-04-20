class Solution(object):#管他个蛋蛋来个排序然后输出他娘的
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[0] #上技巧超长，直接这样反而是比较快的方法