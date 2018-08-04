'''
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#翻转单链表的三种方法：
#https://blog.csdn.net/hyqsong/article/details/49429859
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #原理是从原链表的头部一个一个取节点并插入到新链表的头部
        #实现简单
        ans = None
        p = head
        while p:
            #注意记好四连的写法
            #万年标准题
            tep = p.next
            #当前节点后的链表
            p.next = ans
            #当前节点接新链表
            ans = p
            #写好新链表头部
            p = tep
            #写好剩下的旧链表
        return ans