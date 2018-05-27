'''
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。

示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。

注意:
nums1和nums2中所有元素是唯一的。
nums1和nums2 的数组大小都不超过1000。
'''

class Solution:
    #看图说话法
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums1:
            index2 = nums2.index(i)
            flag = True
            for j in range(index2 + 1, len(nums2)):
                if nums2[j] > i:
                    ans.append(nums2[j])
                    flag = False
                    break

            if flag:
                ans.append(-1)
        return ans

class SolutionBest:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2dict = dict()
        Lr = []
        L = []

        for num2 in nums2:
            while L != [] and L[-1] < num2:
                nums2dict[L.pop()] = num2
            L.append(num2)
        #找到nums2每个元素往右第一个更大的数（如果存在的话）

        for num1 in nums1:
            Lr.append(nums2dict.get(num1, -1))

        return Lr