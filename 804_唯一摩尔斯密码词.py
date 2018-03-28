class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codelist = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                    "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        #摩尔斯密码表
        wordlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        #字母表
        strlist = []
        for word in words:
            code = ''
            for a in word:
                indexa = wordlist.index(a)
                #重点在这，要会写列表查询，得到待查询元素在列表的索引
                code = code + codelist[indexa]
            strlist.append(code)
        setlist = set(strlist)
        return len(setlist)
