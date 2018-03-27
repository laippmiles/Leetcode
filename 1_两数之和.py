class Solution:#暴力便利法，执行时间也很暴力
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums [j] == target:
                    return [i,j]

class SolutionBest:#52ms，比美国佬写得好理解
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keys = {}#核心在借用字典变量保存已经检索过的消息
        for i in range(len(nums)):#整个过程最多跑一遍遍历即可
            if target - nums[i] in keys:
                return ([keys[target-nums[i]],i])
            if nums[i] not in keys:
                keys[nums[i]]=i