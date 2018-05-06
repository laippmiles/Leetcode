'''
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其他所有元素均出现两次。
 找出只出现一次的那两个元素。

示例:
给定 nums = [1, 2, 1, 3, 2, 5], 返回 [3, 5].

注意：
1.结果的顺序并不重要，对于上面的例子 [5, 3] 也是正确答案。
2.你的算法应该具有线性复杂度，
你能否仅使用恒定的空间复杂度来实现它？
'''

class Solution(object):#比较慢
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        dicn = {}
        for i in nums:
            if i not in dicn:
                dicn[i] = 1
            else:
                dicn[i] += 1
        for j in dicn:
            if dicn[j] == 1:
                ans.append(j)
        return ans

class SolutionBest(object):
    #这个用集合更快
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return list(res)