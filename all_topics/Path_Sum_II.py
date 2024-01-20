# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # not work
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    #     if not root:
    #         return []
    #     if root.val > targetSum:
    #         return []
    #     if not root.left and not root.right:
    #         if root.val == targetSum:
    #             return [root.val]
    #         else:
    #             return []

    #     res = []
    #     stack = []
    #     cur_sum = 0

    #     while stack or root:
    #         while root:
    #             cur_sum += root.val
    #             stack.append(root)

    #             # print(cur_sum)
    #             if cur_sum > targetSum:
    #                 break

    #             root = root.left

    #         root = stack.pop()
    #         if cur_sum > targetSum:
    #             cur_sum -= root.val
    #         elif cur_sum == targetSum and stack:
    #             res.append([root.val])
    #             for i in stack:
    #                 res[-1].append(i.val)

    #         # print(cur_sum, root)
    #         root = root.right

    #     return res

    # 深度优先搜索
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret = list()
        path = list()

        def dfs(root: TreeNode, targetSum: int):
            if not root:
                return
            # print(root.val, targetSum)
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                ret.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()

        dfs(root, targetSum)
        return ret

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/path-sum-ii/solutions/427759/lu-jing-zong-he-ii-by-leetcode-solution/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 广度优先搜索
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret = list()
        parent = collections.defaultdict(lambda: None)

        def getPath(node: TreeNode):
            tmp = list()
            while node:
                tmp.append(node.val)
                node = parent[node]
            ret.append(tmp[::-1])

        if not root:
            return ret

        que_node = collections.deque([root])
        que_total = collections.deque([0])

        while que_node:
            node = que_node.popleft()
            rec = que_total.popleft() + node.val

            if not node.left and not node.right:
                if rec == targetSum:
                    getPath(node)
            else:
                if node.left:
                    parent[node.left] = node
                    que_node.append(node.left)
                    que_total.append(rec)
                if node.right:
                    parent[node.right] = node
                    que_node.append(node.right)
                    que_total.append(rec)

        return ret

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/path-sum-ii/solutions/427759/lu-jing-zong-he-ii-by-leetcode-solution/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。