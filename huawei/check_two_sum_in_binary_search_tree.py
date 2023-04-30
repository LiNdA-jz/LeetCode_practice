# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findTarget(self, root: TreeNode, k: int) -> bool:
        # not work
        # if root == None:
        #     return k == 0

        # elif (root.left == None) and (root.right == None):
        #     return root.val == k

        # elif root.left == None:
        #     return (self.findTarget(root.right, k)) or (self.findTarget(root.right, k - root.val))
        # elif root.right == None:
        #     return (self.findTarget(root.left, k)) or (self.findTarget(root.left, k - root.val))

        # else:
        #     return (self.findTarget(root.left, k - root.val)) or (self.findTarget(root.right, k - root.val)) or (self.findTarget(root.left, k)) or (self.findTarget(root.right, k))

    def __init__(self):
        # avoid duplicates
        self.s = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        # check if residual in set
        if k - root.val in self.s:
            return True
        # add root
        self.s.add(root.val)
        # search for left & right
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/opLdQZ/solution/er-cha-sou-suo-shu-zhong-liang-ge-jie-di-bqci/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。