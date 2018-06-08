'''
你是一个专业的小偷，计划偷窃沿街的房屋，
每间房内都藏有一定的现金。
这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，
计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2:
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #此题是198题的扩展
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        #不过因为是房屋是圈状排布，所以分两种情况遍历两次
        #第一次遍历假定偷1室
        #第二次遍历假定不偷1室

        robed1 = [0] * (len(nums))
        #假定偷1室时，其实可以无视最后一个房间
        #这样就能按198的线性动态规划做了
        robed1[1] = nums[0]
        for i in range(2, len(nums)):
            robed1[i] = max(robed1[i - 1], robed1[i - 2] + nums[i - 1])
            #经过第i个房间后的最高收益是下列两个值的较大值
            #经过第i-1个房间的最大收益（没有打劫第i个房间）
            #打劫了第i个房间，第i-2个房间的最高收益及第i个房间金额之和即可
        robed2 = [0] * (len(nums) + 1)
        for i in range(2, len(nums) + 1):
            robed2[i] = max(robed2[i - 1], robed2[i - 2] + nums[i - 1])
            #这是假定不偷1室的情况
        return max(robed1[-1], robed2[-1])


class Solution2(object):
    #空间复杂度为O（1）的做法
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        robed1 = [0] * 2
        robed1[1] = nums[0]
        for i in range(2, len(nums)):
            tep = robed1[1]
            robed1[1] = max(robed1[1], robed1[0] + nums[i - 1])
            robed1[0] = tep

        robed2 = [0] * 2
        for i in range(2, len(nums) + 1):
            tep = robed2[1]
            robed2[1] = max(robed2[1], robed2[0] + nums[i - 1])
            robed2[0] = tep

        return max(robed1[1], robed2[1])