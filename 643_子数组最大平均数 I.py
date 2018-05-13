'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

注意:
1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ans = 0
        sum_sub = 0
        for i in range(len(nums)):
            #用活动窗口法。保存一个新数据后，减掉最老数据的信息
            sum_sub += nums[i]
            if i < k:
                ans = sum_sub
            else:
                sum_sub -= nums[i - k]
                if sum_sub > ans:
                    ans = sum_sub
        return float(ans) / k
        #要精确到小数点后的话，ans要先转float
