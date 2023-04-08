# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # not work
        # if p.val != q.val:
        #     return False
        # else:
        #     if (p.left and q.left) and (p.right and q.right):
        #         return self.isSameTree(p.left, q.left) and (self.isSameTree(p.right, q.right))
        #     elif p.left and q.left:
        #         return self.isSameTree(p.left, q.left)
        #     elif p.right and q.right:
        #         return self.isSameTree(p.right, q.right)
        #     else:
        #         return False


        if p == None and q == None : # Same Tree
            return True
        if p == None or q == None : # Different Size
            return False
        if p.val != q.val : # Different Nodes
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)