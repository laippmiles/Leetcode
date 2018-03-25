class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a,b])
        #注意这里的sum里面只能装可迭代对象，所以把输入的参数装进一个列表里吧
        #参考:https://blog.csdn.net/mjj_1094/article/details/70176173