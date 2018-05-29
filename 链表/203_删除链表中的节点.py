'''
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans.next = head
        ans_head = ans #保存链表头结点位置
        while ans.next:
            #防止最后一个元素没法遍历，只对next进行分析
            #这也是为啥要在head前面随便接一个头结点
            if ans.next.val == val:
                ans.next = ans.next.next
            else:
                ans = ans.next
        return ans_head.next
        #输出next就好了，头结点是方便算法运行随便设的