class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jList = []
        sList = []
        for j in range(len(J)):
            jList.append(J[j])
        for s in range(len(S)):
            sList.append(S[s])
        count = 0

        for stone in sList:#核心做法是这个迭代
            if stone in jList:
                count += 1
        return count

#40ms的示例
class SolutionBest:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        for i in S:#不用这么麻烦，直接迭代查询即可
            if i in J:
                num += 1

        return num
