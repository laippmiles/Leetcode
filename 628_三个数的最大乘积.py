'''
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
示例 1:
输入: [1,2,3]
输出: 6

示例 2:
输入: [1,2,3,4]
输出: 24'''
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()#先给序列排序
        if nums[-1] < 0 or nums[0]>=0:#如果序列全是负数或全是正数，那直接输出后三位数的乘积即可
            return nums[-1]*nums[-2]*nums[-3]
        else:
            #如果序列同时存在负数或正数
            #一正二负可能是nums[-1]*nums[0]*nums[1]如【-20,-10,2,3,4】，也可能是nums[-1]*nums[-2]*nums[-3]如【-1，-2,10,20,30】
            #二正一负的话说明没有多余的正数,那输出永远是nums[-1]*nums[-2]*nums[-3]
            #也可以是纯正数（后三位）
            #因为反正横竖，都是在这两个情况出结果
            #所以直接输出两者较大的值就对了
            return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])

class Solution1(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])#排完序后最大值就这两种表达方式，直接把比较大那个丢出来就完事了

class Solutionbest:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq #heapq是一个独立模块，可以拿来提取最大/最小元素，可对列表进行操作
        #参考https://blog.csdn.net/onlyanyz/article/details/45790235
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0]*a[1]*a[2], a[0]*b[0]*b[1])

a = Solutionbest().maximumProduct([1,2,3,4])
print(a)