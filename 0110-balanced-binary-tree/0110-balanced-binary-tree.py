# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        diff = abs(left_height - right_height)
        # print(left_height)
        # print(right_height)
        # print(diff)
        if diff > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))