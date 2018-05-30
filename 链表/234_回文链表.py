'''
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        def reverseList(root):
            #翻转单链表
            ans = None
            p = root
            while p:
                #底下的四连记好
                tep = p.next
                p.next = ans
                ans = p
                p = tep
            return ans

        half_stop = half = head
        while half_stop and half_stop.next:
            half_stop = half_stop.next.next
            half = half.next
            #我也不晓得为什么，不过整个链表翻转的话是无效的
            #所以只用half指到链表中间部分，然后翻转后半部分的链表

        half_rever = reverseList(half)
        p = head
        p2 = half_rever
        while p and p2:
            #如果前半部分和后半经过翻转的部分相同，这个链表就是回文链表
            if p.val != p2.val:
                return False
            p = p.next
            p2 = p2.next
        return True