'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #应该是第一次做了栈相关的题？
        #还算好理解
        #循环字符串，遇左括号入栈。
        #遇右括号，从栈顶取元素然后配对，判断配对结果。
        #最后再判断栈是否不为空。
        res = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        pair = ['()', '[]', '{}']

        for i in s:
            if i in left:
                res.append(i)
                #左括号入栈
            else:
                if res == []:
                    return False
                    #防止栈是空的，写一个判断
                tep = res.pop() + i
                #右括号出栈配对
                if tep not in pair:
                    return False
        if len(res) != 0:
            return False
        #最后判断是否是空栈
        return True