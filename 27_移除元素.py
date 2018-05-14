'''给定一个数组和一个值，在这个数组中原地移除指定值和返回移除后新的数组长度。

不要为其他数组分配额外空间，你必须使用 O(1) 的额外内存原地修改这个输入数组。

元素的顺序可以改变。超过返回的新的数组长度以外的数据无论是什么都没关系。'''
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[j] = nums[i]
                #思路：j记录的是不相等元素的个数，这句话可以将后面不相等的元素都挪到前j个数组里
                # 第j+1个到时候不读就是了。
                j += 1
        return j

class SolutionBest:
    def removeElement(self , nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
            #remove() 函数用于移除列表中某个值的第一个匹配项。
        return len(nums)

a= Solution()
print(a.removeElement([3,2,2,3],3))