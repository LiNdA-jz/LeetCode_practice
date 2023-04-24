# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # not work
        # if root == None:
        #     return True

        # elif (root.left == None) and (root.right == None):
        #     return True
        # elif (root.left == None):
        #     return False
        # elif (root.right == None):
        #     return False
        # else:
        #     return self.isSymmetric(root.left) and self.isSymmetric(root.right)


        # need extra function!!!!!!!!!!!!!!!
        # Special case...
        if not root:
            return True
        # Return the function recursively...
        return self.isSame(root.left, root.right)
    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, leftroot, rightroot):
        # If both root nodes are null pointers, return true...
        if leftroot == None and rightroot == None:
            return True
        # If exactly one of them is a null node, return false...
        if leftroot == None or rightroot == None:
            return False
        # If root nodes haven't same value, return false...
        if leftroot.val != rightroot.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)