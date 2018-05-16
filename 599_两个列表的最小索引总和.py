'''
假设Andy和Doris想在晚餐时选择一家餐厅，
并且他们都有一个表示最喜爱餐厅的列表，
每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。
 如果答案不止一个，则输出所有答案并且不考虑顺序。
 你可以假设总是存在一个答案。

示例 1:
输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。

示例 2:
输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，
它有最小的索引和1(0+1)。

提示:
1.两个列表的长度范围都在 [1, 1000]内。
2.两个列表中的字符串的长度将在[1，30]的范围内。
3.下标从0开始，到列表的长度减1。
4.两个列表都没有重复的元素。
'''


class Solution(object):
    #有点慢
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dicn = {}
        #老生常谈的哈希表大法
        for i in range(len(list1)):
            if list1[i] not in dicn:
                if list1[i] in list2:
                    dicn[list1[i]] = i
            else:
                dicn[list1[i]] += i
        for j in range(len(list2)):
            if list2[j] not in dicn:
                continue
            else:
                dicn[list2[j]] += j

        dicn = sorted(dicn.items(), key=lambda x: x[1])
        ans = []
        min_num = dicn[0][1]
        for i in dicn:
            if i[1] == min_num:
                ans.append(i[0])
            else:
                break
        return ans


class SolutionBest(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {list1[i]: i for i in range(len(list1))}
        # 推导式先建一个字典里面是，每个元素对应  list1的元素：对应索引
        ans = []
        l = len(list1) + len(list2)
        for i in range(len(list2)):
            if list2[i] in dic:
                m = i + dic[list2[i]]  # 当前索引和
                if m < l:  # 更新最小索引和
                    ans = [list2[i]]  # 索引和一更新，整个ans重写
                    l = m
                elif m == l:
                    ans.append(list2[i])  # 相同最小索引和并列输出

        return ans