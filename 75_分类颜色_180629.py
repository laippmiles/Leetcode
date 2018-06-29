'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

进阶：
1.一个直观的解决方案是使用计数排序的两趟扫描算法。
2.首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
3.你能想出一个仅使用常数空间的一趟扫描算法吗？
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        dicn = {0:0,1:0,2:0}
        #用哈希表解决问题
        for i in nums:
            dicn[i] += 1
        nums[:] = [0]*dicn[0] + [1]*dicn[1] +[2]*dicn[2]
        #注意nums不能直接return，要写[：]赋值