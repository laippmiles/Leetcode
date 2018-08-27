'''

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        #注意做题前考虑特殊情况
        ans = []
        minp = prices[0]
        for i in range(1,len(prices)):
            ans.append(prices[i] - minp)
            #更新每天要是卖出去可能的最大利润
            #minp是在当天前最低的价格，可以在最低价时买
            if prices[i] < minp:
                minp = prices[i]
        return max([max(ans),0])
        #考虑一个大于零的前提，然后ans里的最大数就是答案