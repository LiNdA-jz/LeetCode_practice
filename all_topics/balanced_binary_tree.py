# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # not work
        # height, height_left, height_right = 0, 0, 0

        # if root == None:
        #     return True
        # elif (root.left == None) and (root.right == None):
        #     return True
        # elif root.left == None:
        #     height_right += self.isBalanced(root.right) + 1
        #     return height_right <= 1
        # elif root.right == None:
        #     height_left += self.isBalanced(root.left) + 1
        #     return height_left <= 1
        # else:
        #     height += 1
        #     height_left += self.isBalanced(root.left)
        #     print(height_left)
        #     height_right += self.isBalanced(root.right)
        #     print(height_right)
        #     return abs(height_left - height_right) <= 1

    #     return (self.Height(root) >= 0)
    # def Height(self, root):
    #     if root is None:  return 0
    #     leftheight, rightheight = self.Height(root.left), self.Height(root.right)
    #     if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
    #     return max(leftheight, rightheight) + 1

        def dfs(root):
            if root==None:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]