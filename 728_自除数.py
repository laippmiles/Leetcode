class Solution:#96ms,最直球的解法
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        List = []
        Flag = True
        for i in range(left,right+1):
            stri = str(i)#核心在把数字转成字符串，再转一次int来取位数
            for num in stri:
                num = int(num)
                if num != 0:
                    if i % num != 0:
                        Flag = False
                else:
                    Flag = False
            if Flag:
                List.append(i)
            Flag = True
        return List

#62ms的答案
class Solution62ms:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left, right + 1):
            if '0' not in str(num):
                j = 0
                for i in str(num):
                    if (num % int(i) == 0):
                        j += 1
                    else:
                        break
                if (j == len(str(num))):
                    result.append(num)

        return result