class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in [2,3,5]:
            while num % i == 0:
                num = num/i#对2,3,5这三个因数除到尽为止
        if num == 1:
            return True
        else:
            return False