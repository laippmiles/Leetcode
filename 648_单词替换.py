'''
在英语中，我们有一个叫做 词根(root)的概念，
它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。
例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。
你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，
则用最短的词根替换它。

你需要输出替换之后的句子。
示例 1:
输入: dict(词典) = ["cat", "bat", "rat"]
sentence(句子) = "the cattle was rattled by the battery"
输出: "the cat was rat by the bat"

注:
输入只包含小写字母。
1 <= 字典单词数 <=1000
1 <=  句中词语数 <= 1000
1 <= 词根长度 <= 100
1 <= 句中词语长度 <= 1000
'''

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict.sort()
        #词典先排序
        sentencelist = sentence.split()
        for i in range(len(sentencelist)):
            for j in dict:
                if j in sentencelist[i][:len(j)]:
                    #只检查词根长度的前len(j)个字母
                    sentencelist[i] = j
                    break
        return ' '.join(sentencelist)


class SolutionBetter:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict = set(dict)
        #要先把dict转成集合，要不会超时
        #啥时候去看一眼这个，估计是语言数据结构的问题
        def replace(word):
            for i in range(len(word)):
                if word[:i] in dict:
                    return word[:i]
            else:
                return word

        return ' '.join(map(replace, sentence.split()))
        #重点来了，用了map！
        #map：map() 会根据提供的函数对指定序列做映射。
        #第一个参数 function 以参数序列中的每一个元素调用 function 函数，
        #返回包含每次 function 函数返回值的...
        #Python 2.x 返回列表。
        #Python 3.x 返回迭代器。

        # 例：
        #>>>def square(x) :
        #计算平方数
        #return x ** 2
        # ...
        #map(square, [1,2,3,4,5])    计算列表各个元素的平方
        #[1, 4, 9, 16, 25]
        #map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
        #[1, 4, 9, 16, 25]