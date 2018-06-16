'''
有1000只水桶，其中有且只有一桶装的含有毒药，其余装的都是水。
它们从外观看起来都一样。如果小猪喝了毒药，它会在15分钟内死去。

问题来了，如果需要你在一小时内，弄清楚哪只水桶含有毒药，
你最少需要多少只猪？

回答这个问题，并为下列的进阶问题编写一个通用算法。

进阶:
假设有 n 只水桶，猪饮水中毒后会在 m 分钟内死亡，
你需要多少猪（x）就能在 p 分钟内找出“有毒”水桶？
n只水桶里有且仅有一只有毒的桶。
'''


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        #偏脑筋急转弯的题目
        #注意猪一次性可以同时喝几桶水
        #回想一下矩阵LED那种做法，差不多就是那个
        #详情参考：
        #https://blog.csdn.net/wilschan0201/article/details/72519147
        if buckets == 1:
            return 0

        n = minutesToTest / minutesToDie + 1
        x = 1

        while (n ** x) < buckets:
            x += 1

        return x