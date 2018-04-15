'''给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。

数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。输入:

示例：
letters = ["c", "f", "j"]
target = "a"
输出: "c"
'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        list_a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        index_target = list_a.index(target)
        for i in range(index_target + 1,len(list_a)):
            if list_a[i] in letters:
                return list_a[i]
        return letters[0] #以上查询没找到以后，输出列表第一项

class SolutionBest(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in letters: #题目都说了，有序数组，直接迭代就好
            if i > target:#惊不惊喜，字母之间在python是可以直接“比较大小”的
                return i
        return letters[0]