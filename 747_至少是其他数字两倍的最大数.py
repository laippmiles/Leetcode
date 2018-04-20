'''在一个给定的数组nums中，总是存在一个最大元素 。
查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
如果是，则返回最大元素的索引，否则返回-1。

示例 1:
输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.


示例 2:
输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.'''
class Solution(object):#36ms
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSort = sorted(nums)
        if len(nums) == 1 :
            return 0
        if numSort[-1] != 0 and numSort[-2] == 0:
            return nums.index(numSort[-1])
        if numSort[-1]/numSort[-2] >= 2 :
            return nums.index(numSort[-1])
        else:
            return -1


class SolutionBest(object):#32ms
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [i for i in nums]
        res.sort()
        if len(res) <= 1:
            return 0
        if res[-1] >= res[-2] * 2:#不要用除法，避免要额外写个判断处理0
            return nums.index(res[-1])
        else:
            return -1
