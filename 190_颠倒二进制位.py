'''
颠倒给定的 32 位无符号整数的二进制位。

示例:

输入: 43261596
输出: 964176192
解释: 输入 43261596 二进制表示形式为 00000010100101000001111010011100 ，
      返回 964176192 二进制表示形式为 00111001011110000010100101000000 。
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)[2:]
        n = n[::-1]
        bin0 =(str(0)*32)
        #split分隔符不能用空白的，所以只能一个个append
        list0 = []
        for i in bin0:
            list0.append(i)
        for j in range(len(n)):
            list0[j] = str(int(list0[j]) | int(n[j]))
        n = ''.join(list0[::-1])
        n = n[::-1]
        return int(n,2)

class Solution2:#这个只要32ms
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = reversed(format(n, "b"))
        #format用法参考:
        # https://www.cnblogs.com/wongbingming/p/6848701.html
        #例：format(2, "b")
        #>>> '10'
        #上一句也可以写作：b = (format(n, "b"))[::-1]
        #不过好像没revesed快，慢一点点
        string = ""
        for c in b:
            string += c
            #字符串不可以改元素，但可以用+来增加新的
        while len(string) < 32:
            string += "0"
            #用0补全字符串至32位
        return int(string, 2)