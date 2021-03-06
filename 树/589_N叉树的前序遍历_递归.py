'''
给定一个N叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :
          1
      /  |   \
    3    2    4
  / \
5    6

返回其前序遍历: [1,3,5,6,2,4]。

说明: 递归法很简单，你可以使用迭代法完成此题吗?
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        def order(root):
            if root is None:
                return
            ans.append(root.val)
            for r in root.children:
                order(r)
        order(root)
        return ans