'''
一个长度为 n + 1 的整形数组，其中的数字都在 1 到 n 之间，
包括 1 和 n ，可知至少有一个重复的数字存在。
假设只有一个数字重复，找出这个重复的数字。

注意：
1.不能更改数组内容（假设数组是只读的）。
2.只能使用恒定的额外空间，即要求空间复杂度是 O(1) 。
3.时间复杂度小于 O(n2)
4.数组中只有一个数字重复，但它可能不止一次重复出现。
'''

class Solution(object):
    #采用负数标记法，参考442，用的一个思路

    # 这类问题的一个重要条件就是1 ≤ a[i] ≤ n
    # 用一种正负替换的方法
    # 这类问题的核心是就是找nums[i]和nums[nums[i] - 1]的关系
    # 对于每个nums[i]，我们将其对应的nums[nums[i] - 1]取相反数
    # 如果其已经是负数了，说明之前存在过，我们将其加入结果res中即可

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums[abs(i)-1] < 0:
                return abs(i)
            else:
                nums[abs(i)-1] *= -1