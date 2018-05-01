'''
集合 S 包含从1到 n 的整数。
不幸的是，因为数据错误，
导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，
导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。
你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:
输入: nums = [1,2,2,4]
输出: [2,3]

注意:
1.给定数组的长度范围是 [2, 10000]。
2.给定的数组是无序的。
'''

class Solution(object):#442题+448题出来的结果，慢出翔
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        rangeset = set(range(1,len(nums)+1))
        numset = set(nums)
        loss = list(rangeset - numset)[0]
        for i in nums:
            if nums[abs(i)-1] < 0:
                ans = abs(i)
            else:
                nums[abs(i)-1] *= -1
        return [ans,loss]

class SolutionBest(object):
    #寻找带输出的数字和原数组及1~n数组之间的数学关系，比较讨巧，脑筋急转弯了算是
    class Solution(object):
        def findErrorNums(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            tmp = sum(set(nums))
            twice = sum(nums) - sum(set(nums))
            #到这求出了重复的数据
            lenth = len(nums)
            sumOf1ToN = (lenth + 1) * lenth // 2
            #求1到n的序列总和
            #序列总和减sum(set(nums))即是缺失数字的值了
            return [twice, sumOf1ToN - tmp]