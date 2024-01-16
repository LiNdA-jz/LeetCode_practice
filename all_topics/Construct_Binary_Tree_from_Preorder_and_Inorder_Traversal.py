# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == len(inorder) == 1:
            return TreeNode(preorder[0])

        # print(preorder, inorder)
        root = TreeNode(preorder[0])

        left, right = [], []
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                left = inorder[:i]
                right = inorder[i + 1:]
                break

        m, n = len(left), len(right)
        if m == 0:
            root.left = None
        elif m == 1:
            root.left = TreeNode(left[0])
        else:
            root.left = self.buildTree(preorder[1:m + 1], left)
        if n == 0:
            root.right = None
        elif n == 1:
            root.right = TreeNode(right[0])
        else:
            root.right = self.buildTree(preorder[m + 1:], right)

        return root

    # 递归
    # 在中序遍历中定位到根节点, 分别知道左子树和右子树中的节点数目 -> 递归地对构造出左子树和右子树，再将这两颗子树接到根节点的左右位置
    # 考虑使用哈希表来帮助我们快速地定位根节点
    # 对于哈希映射中的每个键值对，键表示一个元素（节点的值），值表示其在中序遍历中的出现位置
    # 对中序遍历的列表进行一遍扫描
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/255811/cong-qian-xu-yu-zhong-xu-bian-li-xu-lie-gou-zao-9/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 迭代
    # 前序遍历中的任意两个连续节点 u 和 v:
    # v 是 u 的左儿子
    # u 没有左儿子，并且 v 是 u 的某个祖先节点（或者 u 本身）的右儿子
    # 用一个栈 stack 来维护「当前节点的所有还没有考虑过右儿子的祖先节点」，栈顶就是当前节点
    # 只有在栈中的节点才可能连接一个新的右儿子
    # 用一个指针 index 指向中序遍历的某个位置
    # 首先我们将根节点 3 入栈，再初始化 index 所指向的节点为 4
    # 遍历 9。9 一定是栈顶节点 3 的左儿子。我们使用反证法，假设 9 是 3 的右儿子，那么 3 没有左儿子，index 应该恰好指向 3，但实际上为 4，因此产生了矛盾。所以我们将 9 作为 3 的左儿子，并将 9 入栈
    # 遍历 10, index 恰好指向当前的栈顶节点 4 -> 没有左儿子 -> 10 必须为栈中某个节点的右儿子
    # 栈中的节点的顺序和它们在前序遍历中出现的顺序是一致的
    # 每一个节点的右儿子都还没有被遍历过
    # 这些节点的顺序和它们在中序遍历中出现的顺序一定是相反的
    # 栈中的任意一个节点的右儿子还没有被遍历过，说明后者一定是前者左儿子的子树中的节点，那么后者就先于前者出现在中序遍历中
    # 把 index 不断向右移动，并与栈顶节点进行比较, 如果 index 对应的元素恰好等于栈顶节点，那么说明我们在中序遍历中找到了栈顶节点，所以将 index 增加 1 并弹出栈顶节点，直到 index 对应的元素不等于栈顶节点 -> 弹出的最后一个节点 x 就是 10 的双亲节点
    # 依次从栈顶弹出 4，5 和 8，并且将 index 向右移动了三次。我们将 10 作为最后弹出的节点 8 的右儿子，并将 10 入栈
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/255811/cong-qian-xu-yu-zhong-xu-bian-li-xu-lie-gou-zao-9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。