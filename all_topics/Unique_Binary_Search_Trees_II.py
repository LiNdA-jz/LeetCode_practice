# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # not work
    # def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    #     if n == 1:
    #         return [TreeNode(1)]

    #     num_ls = [i for i in range(1, n + 1)]
    #     # print(num_ls)
    #     res = []

    #     def search(cur, left, right):
    #         if cur == None or (len(left) == 0 and len(right) == 0):
    #             return

    #         if len(left) == 1 and len(right) == 1:
    #             cur.left = TreeNode(left[0])
    #             cur.right = TreeNode(right[0])
    #             res.append(bst)
    #             return

    #         # temp = cur
    #         # print(cur)
    #         if len(left) == 0:
    #             cur.left = None
    #             # print(right)
    #             if len(right) == 1:
    #                 cur.right = TreeNode(right[0])
    #                 res.append(bst)
    #                 # return
    #             for i in range(len(right) - 1):
    #                 # print(right, i)
    #                 cur.right = TreeNode(right[i])
    #                 cur = cur.right
    #                 # left = right[:i]
    #                 # right = right[i + 1:]
    #                 # print(left, right)
    #                 search(cur, right[:i], right[i + 1:])
    #                 # cur = temp
    #                 # print(cur)
    #             return

    #         # elif len(left) == 1:
    #         #     cur.left = TreeNode(left[0])

    #         elif len(right) == 0:
    #             cur.right = None
    #             # print(left)
    #             if len(left) == 1:
    #                 cur.left = TreeNode(left[0])
    #                 res.append(bst)
    #                 return
    #             # print(left, len(left))
    #             for i in range(len(left) - 1):
    #                 # print(left, i)
    #                 cur.left = TreeNode(left[i])
    #                 cur = cur.left
    #                 # left = left[:i]
    #                 # right = left[i + 1:]
    #                 # print(left, right)
    #                 search(cur, left[:i], left[i + 1:])
    #                 # cur = temp
    #             return
    #         # elif len(right) == 1:
    #         #     cur.right = TreeNode(right[0])

    #         return

    #     for i in range(1, n + 1):
    #         bst = cur = TreeNode(i)
    #         if i == 1:
    #             left_num = []
    #             right_num = num_ls[1:]
    #         elif i == n:
    #             left_num = num_ls[:i - 1]
    #             right_num = []
    #         else:
    #             left_num = num_ls[:i - 1]
    #             right_num = num_ls[i:]

    #         # print(left_num, right_num)

    #         search(cur, left_num, right_num)

    #     return res

    # 回溯
    # 定义 generateTrees(start, end)，返回序列 [start,end] 生成的所有可行的二叉搜索树
    # i 为当前二叉搜索树的根，那么序列划分为了 [start,i−1] 和 [i+1,end] 两部分，递归调用这两部分

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/unique-binary-search-trees-ii/solutions/339143/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode-solut/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None]

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)

                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)

                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/unique-binary-search-trees-ii/solutions/339143/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode-solut/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。