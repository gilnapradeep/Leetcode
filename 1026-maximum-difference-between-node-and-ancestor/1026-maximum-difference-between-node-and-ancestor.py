# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, mini, maxi):
            if not node:
                return maxi - mini

            mini = min(mini, node.val)
            maxi = max(maxi, node.val)

            return max(
                dfs(node.left, mini, maxi),
                dfs(node.right, mini, maxi)
            )

        return dfs(root, root.val, root.val)