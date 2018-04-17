class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:#防空字符串
            return 0
        lists = [i for i in s.split(' ') if (i != '')]#来个推导式play
        if len(lists) == 0:#防原字符串只有空格
            return 0
        return len(lists[-1])