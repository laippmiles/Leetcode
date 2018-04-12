class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1 :
            return False
        count = 1 #1这个因子在下面的循环是扫不到的
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                count = count + i + num / i #成对提取因子
        if count == num :
            return True
        else:
            return False

class SolutionTimeTLE(object):#记一个超时的例子
        def checkPerfectNumber(self, num):
            """
            :type num: int
            :rtype: bool
            """
            if num <= 1:
                return False
            count = 0
            for i in range(1, num):
                if num % i == 0:
                    count = count + i
            if count == num:
                return True
            else:
                return False