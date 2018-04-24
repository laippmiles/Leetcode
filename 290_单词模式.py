'''给定一种 pattern(模式) 和一个字符串 str ，
判断 str 是否遵循这种模式。
这里的 遵循 指完全匹配，
例如在pattern里的每个字母和字符串 str 中的每个非空单词存在双向单映射关系。

例如：
pattern = "abba", str = "dog cat cat dog", 返回true
pattern = "abba", str = "dog cat cat fish", 返回false.
pattern = "aaaa", str = "dog cat cat dog" , 返回false.
pattern = "abba", str = "dog dog dog dog" , 返回false.
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分开的小写单词。
 '''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lists = str.split(' ')
        if len(pattern)!=len(lists):
            return False
        dics = {}
        for i in range(len(pattern)):
            if pattern[i] not in dics and lists[i] not in dics.values():
                dics[pattern[i]] = lists[i]
            else:
                if pattern[i] not in dics or dics[pattern[i]] != lists[i]:
                    return False
        return True


class SolutionBest(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(' ')
        l1 = len(pattern)
        l2 = len(str_list)
        if l1 != l2:
            return False
        return len(set(zip(pattern,str_list))) == len(set(pattern)) == len(set(str_list))
        #如果键值对的组合数和特征集及单词集 三集集数相同，则说明满足单词模式（这个还是蛮好想象得到的）
        #原理是用了zip：
        # zip() 函数用于将可迭代的对象作为参数，
        # 将对象中对应的元素打包成一个个元组，
        # 然后返回由这些元组组成的列表。
        #a = [1,2,3]
        #b = [4,5,6]
        #c = [4,5,6,7,8]
        #zipped = zip(a,b)
        #[(1, 4), (2, 5), (3, 6)] ：输出打包为元组的列表