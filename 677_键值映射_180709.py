'''

实现一个 MapSum 类里的两个方法，insert 和 sum。

对于方法 insert，你将得到一对（字符串，整数）的键值对。
字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。

对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

示例 1:
输入: insert("apple", 3), 输出: Null
输入: sum("ap"), 输出: 3
输入: insert("app", 2), 输出: Null
输入: sum("ap"), 输出: 5
'''


class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = []

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        for i in range(len(self.dic)):
            if key == self.dic[i][0]:
                self.dic[i][1] = val
                return None
        #这里容易遗漏掉，实现倒不难
        self.dic.append([key, val])

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sumpre = 0
        sizepre = len(prefix)
        for i in range(len(self.dic)):
            if len(self.dic[i][0]) < sizepre:
                continue
            if self.dic[i][0][:sizepre] == prefix:
                sumpre += self.dic[i][1]
        return sumpre

        # Your MapSum object will be instantiated and called as such:
        # obj = MapSum()
        # obj.insert(key,val)
        # param_2 = obj.sum(prefix)