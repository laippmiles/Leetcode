'''
你是产品经理，目前正在领导一个团队开发一个新产品。
不幸的是，您的产品的最新版本没有通过质量检查。
由于每个版本都是基于之前的版本开发的，所以错误版本之后的所有版本都是不好的。

假设你有 n 个版本 [1, 2, ..., n]，
你想找出第一个错误的版本，
导致下面所有的错误。

你可以通过 bool isBadVersion(version) 的接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。您应该尽量减少对 API 的调用次数。
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    #此处AT第374题：猜数游戏，都是用了二分法
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = n
        low = 1
        while low < high:
            mid = (low + high)/2
            tep = isBadVersion(mid)
            if tep == True and isBadVersion(mid-1) == True:
                high = mid - 1
            if tep == True and isBadVersion(mid-1) == False:
                return mid
            if tep == False and isBadVersion(mid-1) == False:
                low = mid + 1
        return high