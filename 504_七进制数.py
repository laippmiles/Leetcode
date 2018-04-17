class Solution(object):#没啥好说的，取余法
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        Flag = False
        listnum = []
        if num < 0 :
            Flag = True
            num *= -1
        pow7 = 0
        while num >= 7 :#这个循环条件应该是全程最难琢磨的了
            listnum.append(str(num%7))
            num /= 7
        listnum.append(str(num%7))
        strnum = ''.join(listnum[::-1])#列表倒置[：：-1]即可
        if Flag:
            return '-' + strnum
        else:
            return strnum