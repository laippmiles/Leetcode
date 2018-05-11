'''
给定一个字符串 S 和一个字符 C。
返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:
输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

说明:
1.字符串 S 的长度范围为 [1, 10000]。
2.C 是一个单字符，且保证是字符串 S 里的字符。
3.S 和 C 中的所有字母均为小写字母。
'''


class Solution(object):
    #过程简单，但是慢（124ms）
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        listC = []
        for i in range(len(S)):
            if S[i] == C:
                listC.append(i)
        ans = []
        for j in range(len(S)):
            #费时的原因主要在这里走了遍历嵌套遍历
            min_dis = len(S)
            for k in listC:
                dis = abs(k - j)
                if dis < min_dis:
                    min_dis = dis
            ans.append(min_dis)
        return ans


class SolutionBetter(object):
    #这个方法只需要正反两次遍历字符串两次
    #参考：
    #http://bookshadow.com/weblog/2018/04/22/leetcode-shortest-distance-to-a-character/
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        N = len(S)
        ans = [N] * N
        lastC = N
        for i in range(N):
            if S[i] == C: lastC = i
            # 第一次因为lastC没更新，之前的索引没有找到"向左"的答案也没事
            #第二次遍历会找到的
            ans[i] = min(ans[i], abs(i - lastC))
        #倒着再遍历一次字符串
        for i in range(N - 1, -1, -1):
            if S[i] == C: lastC = i
            ans[i] = min(ans[i], abs(lastC - i))
        return ans
