# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # mid = len(nums) // 2
        # if len(nums) < 1:
        #     return None
        # btree = TreeNode(nums[mid])

        # left, right = nums[:mid], nums[mid+1:]

        # print(left, right)

        # btree.left = self.sortedArrayToBST(left)
        # btree.right = self.sortedArrayToBST(right)

        # return btree

        # Base condition...
        if len(nums) == 0:
            return None
        # set the middle node...
        mid = len(nums)//2
        # Initialise root node with value same as nums[mid]
        root = TreeNode(nums[mid])
        # Assign left subtrees as the same function called on left subranges...
        root.left = self.sortedArrayToBST(nums[:mid])
        # Assign right subtrees as the same function called on right subranges...
        root.right = self.sortedArrayToBST(nums[mid+1:])
        # Return the root node...
        return root