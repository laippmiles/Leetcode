class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
        #使用int函数，指定进制转换为十进制。
        #输出恒为十进制，输入时有int（a,n）a：待转的数字，n：a的进制