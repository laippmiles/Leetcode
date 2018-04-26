'''给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）,
 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]
输出:
[2,3]'''


class Solution(object):#慢得令人发指
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dicn = {}
        ans = []
        for i in nums:
            if i not in dicn:
                dicn[i] = 1
            else:
                dicn[i] += 1
        for i in dicn:
            if dicn[i] == 2:
                ans.append(i)
        return ans

class Solution2(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dicn = {}
        ans = []
        for i in nums:
            if i not in dicn:
                dicn[i] = 1
            else: dicn[i] += 1
        return [j for j in dicn if dicn[j] == 2] #最后用推导式可以快一点


class SolutionBest(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #参考网址：https://www.cnblogs.com/grandyang/p/6209746.html
        #这类问题的一个重要条件就是1 ≤ a[i] ≤ n
        #用一种正负替换的方法
        #这类问题的核心是就是找nums[i]和nums[nums[i] - 1]的关系
        #对于每个nums[i]，我们将其对应的nums[nums[i] - 1]取相反数
        #如果其已经是负数了，说明之前存在过，我们将其加入结果res中即可
        ans = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                ans.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return ans
