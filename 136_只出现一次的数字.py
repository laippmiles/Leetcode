#如何在使用O(n)的时间复杂度和O(0)的额外空间复杂度来找到一个数组中唯一一个成单的数字。
#参考：https://segmentfault.com/a/1190000010669987
class SolutionSort:#有序列表法
    #如果将array排序后，那么相同的数字一定位于相邻的位置上
    # 只需要比较2k和2k+1位置上的值是否相同就可以了。
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0] #如果列表只有一个元素，那直接输出
        nums.sort()#列表排序
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[len(nums)-1]#上面的循环是不管最后一个元素的，上面要是输不出，那说明就是最后一个元素了

#这里就需要提一下异或这个操作符。一个数值和另一个数值进行两次异或计算，该数值不变。
# 也就是说： A XOR B XOR B = A XOR （B XOR B） = A
#其实异或的话，可以用白话来说就是‘要么这个，要么那个’
#所以也就是说，如果将array中的所有数值都进行一次异或计算
# 那么最终的结果也就是那个singleNumber。
class SolutionXOR:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xornum = 0
        for num in nums:
            xornum ^= num
        return xornum