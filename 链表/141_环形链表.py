'''
给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #用两个指针，一个跑的快一个跑的慢，
        #那么如果有环的话，跑的快的一定会追满的一圈。
        #参考：
        #https://blog.csdn.net/qq_33168253/article/details/79890199
        slow = fast = head
        while fast and fast.next:
            #用这种双指针循环时，注意停止迭代的方法是判断快的那个指针的本身及其next
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
