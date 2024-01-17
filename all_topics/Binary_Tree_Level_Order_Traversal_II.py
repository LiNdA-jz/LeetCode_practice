# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # not work
    # def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []

    #     res = []
    #     cur = 0
    #     stack = []

    #     while stack or root:
    #         if not root:
    #             cur -= 1

    #         while root:
    #             stack.append(root)
    #             if cur >= len(res):
    #                 res.append([root.val])
    #                 cur += 1
    #             else:
    #                 res[cur].append(root.val)
    #                 if root.left or root.right:
    #                     cur += 1
    #             root = root.left

    #         root = stack.pop()
    #         root = root.right

    #     return res[::-1]

    # 广度优先搜索
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levelOrder = list()
        if not root:
            return levelOrder

        q = collections.deque([root])
        while q:
            level = list()
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelOrder.append(level)

        return levelOrder[::-1]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/solutions/402560/er-cha-shu-de-ceng-ci-bian-li-ii-by-leetcode-solut/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。