'''
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，
试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。
'''

# The rand7() API is already defined for you.
def rand7():
    import random
    return random.randint(1,7)

'''
（rand7（）-1）*7 + rand7（）
rand7（）- 1获得一个离散整数凑集{0，1，2，3，4，5，6}
（rand7（）-1）*7获得一个离散整数凑集A={0，7，14，21，28，35，42}
rand7（）获得的凑集B={1，2，3，4，5，6，7}
此时A和B中的元素互相独立，
因为A和B中的任意元素相加，得到的结果是不重复的。
按照互相独立的概率公式P（AB）=P（A）P（B）计算。
（rand7（）-1）*7+rand7（）生成1-49之间，每个数的概率都是1/49。
'''
#https://blog.csdn.net/u013630349/article/details/47947531
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        x = (rand7()-1)*7 + rand7()
        while x > 40:
            x = (rand7()-1)*7 + rand7()
        return x % 10 + 1