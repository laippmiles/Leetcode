'''
给定一个整数数组和一个整数 k，
判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:
输入: [1,2,3,1], k = 3
输出: true

示例 2:
输入: [1,0,1,1], k = 1
输出: true

示例 3:
输入: [1,2,1], k = 0
输出: false
'''

#参考：
# https://blog.csdn.net/xiangwanpeng/article/details/52953537
class Solution(object):#慢
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k <= 0:#其实是不需要这两个判断的
            return False
        dicn = {}
        for i in range(len(nums)):
            if nums[i] in dicn  and  (i - dicn[nums[i]])<=k :
                return True
            else:
                dicn[nums[i]] = i
        return False

class Solution2(object):#正常答案
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dicn = {}
        for i in range(len(nums)):
            if nums[i] in dicn  and  (i - dicn[nums[i]])<=k :
                #对新遍历到的元素对比它在字典存着的上一个相同元素的索引
                return True
            else:
                dicn[nums[i]] = i
                #要是没找到符合要求的i，j，就记下现在相应的索引
        return False