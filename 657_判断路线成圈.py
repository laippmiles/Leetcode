'''
初始位置 (0, 0) 处有一个机器人。
给出它的一系列动作，判断这个机器人的移动路线是否形成一个圆圈，
换言之就是判断它是否会移回到原来的位置。
移动顺序由一个字符串表示。
每一个动作都是由一个字符来表示的。
机器人有效的动作有 R（右），L（左），U（上）和 D（下）。
输出应为 true 或 false，表示机器人移动路线是否成圈。

示例 1:
输入: "UD"
输出: true

示例 2:
输入: "LL"
输出: false
'''
class Solution(object):
    #原理都是一个东西，用内置会快很多。
    #可我觉得真算时间复杂度的话，应该都是O(n)级哎..？
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        countR = 0
        countL = 0
        countU = 0
        countD = 0
        for i in moves:
            if i == 'R':
                countR += 1
            elif i == 'L':
                countL += 1
            elif i == 'U':
                countU += 1
            elif i == 'D':
                countD += 1
        if countR == countL and countU == countD:
            return True
        else:
            return False

class SolutionFaster(object):
    #这个可能是用了内置，反正快很多
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')) or False