'''
设计一个支持 push，pop，top 操作，
并能在常数时间内检索到最小元素的栈。

1.push(x) -- 将元素 x 推入栈中。
2.pop() -- 删除栈顶的元素。
3.top() -- 获取栈顶元素。
4.getMin() -- 检索栈中的最小元素。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''

#参考：
#https://www.cnblogs.com/baiyb/p/8443337.html
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minnumlist = []
        #用最小栈的方法找最小值
        self.minnum = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.stack) == 1:
            self.minnumlist.append(x)
            self.minnum = x
            #最小栈是一个降序数组
        if x <= self.minnumlist[-1]:
            self.minnumlist.append(x)
            self.minnum = x

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.minnumlist[-1]:
            self.minnumlist.pop()
            if len(self.minnumlist) == 0:
                self.minnum = None
            else:
                self.minnum = self.minnumlist[-1]
        #删除栈顶的元素时要考虑栈顶元素可能和最小栈相关
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minnum


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()