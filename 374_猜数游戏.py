#我们正在玩猜数游戏。 游戏如下：
#我从 1 到 n 选择一个数字。 你需要猜我选择了哪个号码。
#每次你猜错了，我会告诉你这个数字是高还是低。
#你调用一个预定义的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
#-1 : 我的数字比较低
# 1 : 我的数字比较高
# 0 : 恭喜！你猜对了！
#如n = 10, 我选择 6.
#返回 6.
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = n
        low = 1
        while  low < high:
            mid = (high + low)/2
            tep = guess(mid)
            if tep == 1:
                low = mid + 1#二分法建议自己画图，一下就懂了
                #左右象限更新方向是由内靠拢的
            elif tep == -1:
                high = mid - 1
            else:
                return mid
        return high
