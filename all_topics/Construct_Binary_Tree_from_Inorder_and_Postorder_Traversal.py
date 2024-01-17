# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) <= 0:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        # print(inorder, postorder)
        # print(postorder, postorder[-1])
        root = TreeNode(postorder[-1])
        left, right = [], []
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                left = inorder[:i]
                right = inorder[i + 1:] if i + 1 < len(inorder) else []
                break

        # print(left, right)
        m, n = len(left), len(right)
        # if m == 1:
        #     root.left = TreeNode(left[0])
        # else:
        root.left = self.buildTree(left, postorder[:m])
        # if n == 1:
        #     root.right = TreeNode(right[0])
        # else:
        root.right = self.buildTree(right, postorder[m:-1])

        return root

    # 递归
    # 后序遍历的数组最后一个元素代表的即为根节点
    # 利用已知的根节点信息在中序遍历的数组中找到根节点所在的下标, 根据其将中序遍历的数组分成左右两部分
    # 创建哈希表来存储中序序列
    # helper(in_left, in_right)
    # 如果 in_left > in_right，说明子树为空，返回空节点
    # 选择后序遍历的最后一个节点作为根节点
    # 利用哈希表 O(1)O(1)O(1) 查询当根节点在中序遍历中下标为 index。从 in_left 到 index - 1 属于左子树，从 index + 1 到 in_right 属于右子树
    # 递归创建右子树 helper(index + 1, in_right) 和左子树 helper(in_left, index - 1)
    # 需要先创建右子树，再创建左子树的依赖关系
    # 按每次选择「后序遍历的最后一个节点」为根节点，则先被构造出来的应该为右子树
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None

            # 选择 post_idx 位置的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            index = idx_map[val]

            # 构造右子树
            root.right = helper(index + 1, in_right)
            # 构造左子树
            root.left = helper(in_left, index - 1)
            return root

        # 建立（元素，下标）键值对的哈希表
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solutions/426738/cong-zhong-xu-yu-hou-xu-bian-li-xu-lie-gou-zao-14/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 迭代
    # 如果将中序遍历反序，则得到反向的中序遍历，即每次遍历右孩子，再遍历根节点，最后遍历左孩子
    # 如果将后序遍历反序，则得到反向的前序遍历，即每次遍历根节点，再遍历右孩子，最后遍历左孩子
    # 「反向」的意思是交换遍历左孩子和右孩子的顺序，即反向的遍历中
    # 后序遍历中的任意两个连续节点 u 和 v
    # u 是 v 的右儿子
    # v 没有右儿子，并且 u 是 v 的某个祖先节点（或者 v 本身）的左儿子。如果 v 没有右儿子，那么上一个遍历的节点就是 v 的左儿子。如果 v 没有左儿子，则从 v 开始向上遍历 v 的祖先节点，直到遇到一个有左儿子（且 v 不在它的左儿子的子树中）的节点 va ，那么 u 就是 va 的左儿子
    # 用一个栈和一个指针辅助进行二叉树的构造
    # 依次枚举后序遍历中除了第一个节点以外的每个节点。如果 index 恰好指向栈顶节点，那么我们不断地弹出栈顶节点并向左移动 index，并将当前节点作为最后一个弹出的节点的左儿子；如果 index 和栈顶节点不同，我们将当前节点作为栈顶节点的右儿子
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        s = [root]

        inorderIndex = len(inorder) - 1

        for i in range(len(postorder) - 2, -1, -1):
            postorderVal = postorder[i]
            node = s[-1]

            if node.val != inorder[inorderIndex]:
                node.right = TreeNode(postorderVal)
                s.append(node.right)
            else:
                while s and s[-1].val == inorder[inorderIndex]:
                    node = s.pop()
                    inorderIndex -= 1
                node.left = TreeNode(postorderVal)
                s.append(node.left)

        return root