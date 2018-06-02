'''
给定一个字符串S，通过将字符串S中的每个字母转变大小写，
我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]

注意：
1.S 的长度不超过12。
2.S 仅由数字和字母组成。
'''

#来啦！超典型的递归题
#请全文熟读并背诵！

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if S == '' :
            return[S]
        else:
            rest = self.letterCasePermutation(S[1:])
        #这么写递归条件就很清楚了
        #重点在这！递归不要自己在脑海死轴，确实理不清就画图吧
        #这个递归直接就是自身调用了
        if S[0].isalpha():
            return [(S[0].upper() + s) for s in rest] + [(S[0].lower() + s) for s in rest]
        else:
            return [(S[0] + s) for s in rest]
            #第一个字母是最外层，这个return是输出的