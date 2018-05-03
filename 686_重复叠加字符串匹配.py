'''
给定两个字符串 A 和 B,
寻找重复叠加字符串A的最小次数，
使得字符串B成为叠加后的字符串A的子串，
如果不存在则返回 -1。

举个例子，A = "abcd"，B = "cdabcdab"。

答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。

注意:
 A 与 B 字符串的长度在1和10000区间范围内。
 '''

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A:
            return 1
        count = 1
        APlus = A
        while B not in A:
            count += 1
            APlus = APlus + A #每叠加一次判断一次
            if B in APlus:
                return count
            elif len(B)*3 < len(APlus):
                #这个3倍应是经验值，实属无奈才这么写
                return -1


class SolutionBest(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        adic = {}
        bdic = {}
        #又是用字典大法
        for i in A:
            if i not in adic:
                #统计字符串A的元素状况
                adic[i] = 1
            else:
                adic[i] += 1
        for j in B:
            if j not in bdic:
                # 统计字符串B的元素状况
                bdic[j] = 1
            else:
                bdic[j] += 1
        n = 1
        for k in bdic.keys():
            if k not in adic:
                return -1
            else:
                pown = (adic[k] + bdic[k] - 1) // adic[k]#主要要记住这里
                #这个代码是：
                #https://leetcode.com/articles/repeated-string-match/
                #的改进状况
                if pown > n:
                    n = pown
        ans = A * n
        if B in ans:
            return n
        else:
            ans = ans + A
            if B in ans:
                return n + 1
                #如果B是A重复字符串的子串的话，只有上述两种可能
            else:
                return -1


#a = SolutionBest()
#a.repeatedStringMatch("abcd","cdabcdab")