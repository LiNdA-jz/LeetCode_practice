# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # not work
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     def check(root, left, node):
    #         if root.left == None and root.right == None:
    #             if left and root.val >= node:
    #                 return False
    #             elif not left and root.val <= node:
    #                 return False
    #             else:
    #                 return True

    #         elif root.left == None:
    #             if root.right.val <= root.val:
    #                 return False
    #             return check(root.right, left, max(node, root.val))

    #         elif root.right == None:
    #             if root.left.val >= root.val:
    #                 return False
    #             return check(root.left, left, min(node, root.val))

    #         else:
    #             if root.left.val >= root.val or root.right.val <= root.val:
    #                 return False
    #             if left:
    #                 if root.right.val >= node:
    #                     return False
    #             else:
    #                 if root.left.val <= node:
    #                     return False
    #             return check(root.left, left, node) and check(root.right, left, node)

    #     if root.left == None and root.right == None:
    #         return True
    #     elif root.left == None:
    #         if root.right.val <= root.val:
    #             return False
    #         return check(root.right, False, root.val)
    #     elif root.right == None:
    #         if root.left.val >= root.val:
    #             return False
    #         return check(root.left, True, root.val)
    #     else:
    #         return check(root.left, True, root.val) and check(root.right, False, root.val)

    # 递归
    # helper(root, lower, upper)
    # 递归调用左子树时，我们需要把上界 upper 改为 root.val -> helper(root.left, lower, root.val)
    # 入口为 helper(root, -inf, +inf)
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')) -> bool:
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/validate-binary-search-tree/solutions/230256/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 中序遍历
    # 中序遍历」得到的值构成的序列一定是升序的 -> 检查当前节点的值是否大于前一个中序遍历到的节点的值即可
    # 使用栈来模拟中序遍历的过程
    # 先遍历左子树，再遍历根节点，最后遍历右子树
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/validate-binary-search-tree/solutions/230256/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。