# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth, depth_left, depth_right = 0, 0, 0
        # if root == None:
        #     return 0

        # if (root.left == None) and (root.right == None):
        #     depth += 1
        # elif (root.right == None):
        #     depth += self.maxDepth(root.left) + 1
        # elif (root.left == None):
        #     depth += self.maxDepth(root.right) + 1
        # else:
        #     depth_left += self.maxDepth(root.left)
        #     print(root.val, depth_left)
        #     depth_right +=  self.maxDepth(root.right)
        #     print(root.val, depth_right)
        #     depth += max(depth_left, depth_right) + 1

        # return depth

        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1