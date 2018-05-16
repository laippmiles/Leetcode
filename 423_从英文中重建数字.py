'''
给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。
按升序输出原始的数字。

注意:
1.输入只包含小写英文字母。
2.输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
3.输入字符串的长度小于 50,000。

示例 1:
输入: "owoztneoer"
输出: "012" (zeroonetwo)

示例 2:
输入: "fviefuro"
输出: "45" (fourfive)
'''
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        #用参考：
        #https://www.cnblogs.com/grandyang/p/5996239.html
        #的方法
        dicn = {}
        alpha = 'hzerontfuixvgws'
        for a in alpha:
            dicn[a] = 0
        for i in s:
                dicn[i] += 1
        ans = [0,0,0,0,0,0,0,0,0,0]
        ans[0] = dicn['z']
        ans[2] = dicn['w']
        ans[4] = dicn['u']
        ans[1] = dicn['o'] - ans[0] - ans[2] -ans[4]
        ans[6] = dicn['x']
        ans[8] = dicn['g']
        ans[5] = dicn['f'] - ans[4]
        ans[7] = dicn['v'] - ans[5]
        ans[3] = dicn['r'] - ans[0] - ans[4]
        ans[9] = dicn['i'] - ans[5] - ans[6] - ans[8]
        strans = ''
        for j in range(len(ans)):
            strans += str(j) * ans[j]
        return strans