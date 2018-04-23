'''给定两个数组，写一个方法来计算它们的交集。

例如:
给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

注意：
1.输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
2.我们可以不考虑输出结果的顺序。'''


class Solution(object):#瞎几把写的直感暴力法，120ms排名后6%惨不忍睹
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 == [] or nums2 == []:
            return []
        setl = set(nums1 + nums2)
        num3 = []
        for i in setl:
            if i in nums1 and i in nums2:
                count = min(nums1.count(i), nums2.count(i))
                for j in range(count):
                    num3.append(i)
        return num3


class SolutionBest(object):#36ms
    #原理是利用字典，先对其中一个数组统计元素频率
    #再遍历另一个数组，最后构造输出列表即可
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = {}
        for x in nums1:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1

        res = []
        for x in nums2:
            if x in m and m[x] > 0:
                res.append(x)
                m[x] -= 1
        return res
