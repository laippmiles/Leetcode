'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，
使得 num1 成为一个有序数组。

说明:
1.初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
2.你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #参考：
        #https://www.cnblogs.com/lightwindy/p/8503687.html
        #不用新建立数组，而是直接在A 数组上写入，
        # 因为 A 足够大，可从两个数组的最大数也就是最后一个数开始比较，
        # 大的写入A[m + n -1]，然后循环这个过程。
        # 如果 B 的元素写完了，A 剩下的元素正好在正取的位置，不用写了。
        # 如果 A 的元素都取完了，那剩下的 B 的元素可一次全部写进 A。
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        if n > 0:
            nums1[:n] = nums2[:n]