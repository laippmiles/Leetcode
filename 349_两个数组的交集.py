'''给定两个数组，写一个函数来计算它们的交集。

例子:
 给定 num1= [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].

提示:
1.每个在结果中的元素必定是唯一的。
2.我们可以不考虑输出结果的顺序。
'''

class Solution(object):#瞎几把写的后百分之五
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1==[] or nums2 ==[]:
            return []
        setl = set(nums1+nums2)
        num3 = []
        for i in setl:
            if i in nums1 and i in nums2:
                num3.append(i)
        return num3

class SolutionBest(object):#注意到提示的内容，这个实际上是集合运算
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))