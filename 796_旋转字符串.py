class Solution:#这一题重点在会找索引点
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        if len(A) != len(B):
            return False
        for i in range(len(A)):
            b = A[i:] + A[0:i]#字符串提取索引是左开右闭的
            if b == B:
                return True
        return False
#测试代码
a = Solution()
b = a.rotateString('abcde','cdeab')
print(b)