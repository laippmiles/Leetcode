'''
你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金
，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，
计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
'''

class Solution(object):
    #这题是基础的动态规划题
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        robed = [0] * (len(nums)+1)
        #保存经过第一个房间后能得到的最多收益
        robed[1] = nums[0]
        #经过第0个房间收益为0
        #经过第一个房间最高收益就是第一个房间的钱本身
        if len(nums) == 1:
            return robed[1]
        for i in range(2,len(nums)+1):
            robed[i] = max(robed[i-1],robed[i-2]+nums[i-1])
            #经过第i个房间后的最高收益是下列两个值的较大值
            #经过第i-1个房间的最大收益（没有打劫第i个房间）
            #打劫了第i个房间，第i-2个房间的最高收益及第i个房间金额之和即可
        return robed[-1]

class Solution2(object):
    #原理一致，这里改成空间复杂度为O（n）的方法
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        pre = 0
        now = nums[0]
        if len(nums) == 1:
            return now
        for i in range(2,len(nums)+1):
            tep = now
            now = max(now,pre + nums[i-1])
            pre = tep
        return now