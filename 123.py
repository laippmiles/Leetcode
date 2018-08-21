# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        head = pHead
        p = pHead
        while P is not None:
            if p.next is not None:
                if p.val == p.next.val:
                    p.val = p.next.val
                    p.next = p.next.next
            p = p.next
        return head

a = Solution()
a.deleteDuplication({1,2,3,3,4,4,5})