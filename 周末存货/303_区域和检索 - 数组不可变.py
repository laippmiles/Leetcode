'''
给定一个整数数组  nums，
求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。
'''

class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)

class NumArray2:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = []
        count = 0
        for i in nums:
            count += i
            self.sums.append(count)
            #注意到sumRange要多次调用
            #所以先在第一次遍历把总和相关的信息保存下来会更快

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return (self.sums[j] - self.sums[i - 1]) if i > 0 else self.sums[j]
        #用了python式的写法，以后尽量多试试这种吧
        #这里主要是防止i=0执行i-1会索引超出范围



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)