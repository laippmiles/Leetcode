'''
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，
判断二者是否相等，并返回结果。 # 代表退格字符。


示例 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。

示例 2：
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。

示例 3：
输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。

示例 4：
输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。

提示：
1.1 <= S.length <= 200
2.1 <= T.length <= 200
3.S 和 T 只含有小写字母以及字符 '#'。
'''


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        ans1 = ''
        ans2 = ''
        #千万别想多，看图说话即可
        #参考：
        #https://blog.csdn.net/fuxuemingzhu/article/details/80643408
        for i in S:
            if i == '#':
                if ans1:
                    ans1 = ans1[:-1]
            else:
                ans1 = ans1 + i

        for j in T:
            if j == '#':
                if ans2:
                    ans2 = ans2[:-1]
            else:
                ans2 = ans2 + j

        if ans1 == ans2:
            return True
        else:
            return False