#给出一个包含 0, 1, 2, ..., n 中 n 个数的序列
# 找出 0 .. n 中没有出现在序列中的那个数。
#输入: [3,0,1]，输出: 2

class Solution1:#96ms
    #最直感的做法，其实不用这么搞的。主要是用不着sort，浪费时间
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

class Solution:#68ms
    #脑筋急转弯做法，一看就知道怎么回事了
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumList = sum(nums)
        sumNum = 0
        for i in range(len(nums)+1):
            sumNum += i
        return sumNum - sumList