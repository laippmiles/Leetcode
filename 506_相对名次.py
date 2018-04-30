'''
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。
前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”
（"Gold Medal", "Silver Medal", "Bronze Medal"）。
(注：分数越高的选手，排名越靠前。)

示例 1:
输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。

提示:
1.N 是一个正整数并且不会超过 10000。
2.所有运动员的成绩都不相同。
'''
class Solution(object):#这个方法极慢，要828ms
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        num = sorted(nums , reverse = True)
        for i in range(len(num)):
            index = nums.index(num[i])
            if i == 0:
                nums[index] = 'Gold Medal'
            elif i == 1:
                nums[index] = 'Silver Medal'
            elif i == 2:
                nums[index] = 'Bronze Medal'
            else:
                nums[index] = str(i + 1)
        return nums

class Solution2(object):#用了枚举enumerate和推导式实现算法
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dicn = {}#再现字典大法
        num = sorted(nums,reverse = True)
        for i , num in enumerate(num):
            #enumerate介绍：https://blog.csdn.net/churximi/article/details/51648388
            #如果对一个列表，既要遍历索引又要遍历元素时
            #举例
            '''
            list1 = ["这", "是", "一个", "测试"]
            for  index, item in enumerate(list1):
                print index, item
            >>>
            0 这
            1 是
            2 一个
            3 测试
            '''
            if i == 0:
                dicn[num] = 'Gold Medal'
            elif i == 1:
                dicn[num] = 'Silver Medal'
            elif i == 2:
                dicn[num] = 'Bronze Medal'
            else:
                dicn[num] = str(i + 1)
        return [dicn[n] for n in nums]#用推导式输出答案