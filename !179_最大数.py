'''

给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:
输入: [10,2]
输出: 210

示例 2:
输入: [3,30,34,5,9]
输出: 9534330

说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def funcstr(a,b):
            #compare(x,y)函数会在x<y时返回负数，
            #在x>y时返回正数，如果x=y则返回0（根据你的定义）
            if int(a+b) < int(b+a):
                return 1
            elif int(a+b) > int(b+a):
                return -1
            else:
                return 0
        #原来！sort的规则是可以自己定的！！
        #参考：
        #
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        #在sort里写cmp参数就能用自定义排序了
        #通常默认sort是升序
        nums.sort(cmp = funcstr)
        ans = ''
        for j in nums:
            ans += j
        if int(ans) == 0:
            return '0'
        return ans