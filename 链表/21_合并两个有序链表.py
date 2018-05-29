'''
将两个有序链表合并为一个新的有序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        #建一个头结点，头结点里头的初值随意
        ans_head = ans
        #记录输出链表的头部，其.next所指的就是需要输出的答案

        while l1 and l2:
            if l1.val < l2.val:
                ans.next = l1
                l1 = l1.next
                #将l1所指移到下个节点（配合C语言的指针理解就很好懂了）
            else:
                ans.next = l2
                l2 = l2.next
                #将l2所指移到下个节点
            ans = ans.next
            #记得要写这句，将ans所指移到下个节点
        if l1:
            #l1还有剩下的话，直接接到ans后面就好，如果剩的是l2也是同理
            ans.next = l1
        if l2:
            ans.next = l2
        return ans_head.next
        #注意不是输出ans_head，而是输出ans_head.next