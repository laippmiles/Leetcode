'''给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。请注意，返回的下标值（index1 和 index2）不是从零开始的。

你可以假设每个输入都只有一个解决方案，而且你不会重复使用相同的元素。

输入：数组 = {2, 7, 11, 15}, 目标数 = 9
输出：index1 = 1, index2 = 2'''


'''思路：
这题的输入是有序数组，限定了一定会有解，
用双指针来做，定义左右两个指针，左指针指向第一个数，右指针指向最后一个数，
然后用这两个数的和与Target比较，
如果比Target小，左指针向右移一位，
如果比Target大，右指针向左移一位。
然后再进行比较，直到找到或者两个指针相遇为止。'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1
        while start != end:
            if numbers[start] + numbers[end] == target :
                return [start+1,end+1]
            elif numbers[start] + numbers[end] < target :
                start += 1
            else:
                end -= 1