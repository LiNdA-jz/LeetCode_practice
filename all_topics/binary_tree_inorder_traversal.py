# In inorder, the order should be
# left -> root -> right
#
# But when we use stack, the order should be reversed:
#
# right -> root -> left

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # not work
        # if not root:
        #     return []

        # res = [root.val]
        # while root.left:
        #     root = root.left
        #     res = self.inorderTraversal(root)
        # while root.right:
        #     root = root.right
        #     res = self.inorderTraversal(root)
        # res.append(root.val)

        # return res

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []