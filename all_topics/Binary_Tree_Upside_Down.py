# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        cur = root
        stack = []
        while cur.left:
            stack.append(cur)
            cur = cur.left
            # print(stack)

        # print(cur, len(stack))
        new_root = cur
        while stack:
            prev = stack.pop()
            # print(prev)
            cur.left = prev.right
            cur.right = prev
            prev.left = None
            prev.right = None

            # print(cur)

            cur = prev

        return new_root

    # 自底向上迭代
    # 题目要求二叉树满足如果右节点存在那么一定是叶节点，因此二叉树的最左侧的叶节点一定位于最大层数，且最左侧的叶节点是翻转后的二叉树的根节点
    # 在找到最左侧的叶节点的过程中，使用一个栈存储访问到的所有节点
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root.left is None and root.right is None:
            return root
        stack = []
        temp = root
        while temp is not None:
            stack.append(temp)
            temp = temp.left
        newRoot = stack[-1]
        stack.pop()
        while len(stack) > 0:
            node = stack[-1]
            stack.pop()
            prevLeft, prevRight = node.left, node.right
            prevLeft.left, prevLeft.right = prevRight, node
            if prevRight is not None:
                prevRight.left = None
                prevRight.right = None
            node.left = None
            node.right = None
        return newRoot

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/binary-tree-upside-down/solutions/2477581/shang-xia-fan-zhuan-er-cha-shu-by-leetco-vmk9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 递归
    # 一个有子节点的节点一共会存在 2 种状态，左节点必然存在，右节点可能存在
    # 经过翻转左节点会变成父节点，右节点会变成左节点，父节点变成右节点
    # 每次都只需要翻转左子节点，所以我们可以将第一次翻转的三个节点打包成一个节点看做根节点，那么向下需要翻转的结构就又变成了上面的结构，继续向下翻转即可
    # 先递归到最下面再交换上一层的节点
    # 1. 保存当前节点的左右子节点。
    # 2. 调用递归函数翻转左子节点，返回翻转后的根节点。
    # 3. 按照上面的要求翻转当前节点。
    # 4. 返回根节点。
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root.left is None:
            return root
        left, right = root.left, root.right
        ret = self.upsideDownBinaryTree(left)
        left.left, left.right = right, root
        root.left, root.right = None, None
        return ret

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/binary-tree-upside-down/solutions/2477581/shang-xia-fan-zhuan-er-cha-shu-by-leetco-vmk9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。