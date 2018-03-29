class Solution:#980ms+
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        num = 0
        for guy in g:
            for bingan in s:
                if bingan >= guy:
                    num += 1
                    s.remove(bingan)
                    break
        return num

class SolutionBest:#直接直感用两个标识只遍历一遍，上一个答案装逼过头反而是平方的慢
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        guy = 0
        bingan = 0
        print(len(g))
        print(len(s))
        while guy < (len(g)-1) or bingan < (len(s)-1):
            print('guy',guy)
            print('bingan',bingan)
            if g[guy] <= s[bingan]:
                guy += 1
                bingan += 1
            else:
                bingan += 1
        return guy
a = SolutionBest()
print(a.findContentChildren([1,2,3],[1,1]))