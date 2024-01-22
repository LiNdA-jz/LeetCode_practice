# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return

        def stack(root):
            stack = []
            res = []

            while stack or root:
                while root:
                    stack.append(root)
                    res.append(root.val)
                    root = root.left

                root = stack.pop()
                root = root.right

            return res

        stk = stack(root)
        # print(stk)

        stk.pop(0)

        while stk:
            root.left = None
            root.right = TreeNode(stk.pop(0))
            root = root.right

    # 前序遍历
    # 递归
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

    # 迭代
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()
        stack = list()
        node = root

        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 前序遍历和展开同步进行
    # 在对左子树进行遍历时，没有存储右子节点的信息
    # 只要对前序遍历进行修改，在遍历左子树之前就获得左右子节点的信息，并存入栈内，子节点的信息就不会丢失，就可以将前序遍历和展开为单链表同时进行。
    # 不适用于递归实现的前序遍历，只适用于迭代实现的前序遍历
    # 每次从栈内弹出一个节点作为当前访问的节点，获得该节点的子节点，如果子节点不为空，则依次将右子节点和左子节点压入栈内（注意入栈顺序）
    # 维护上一个访问的节点 prev，每次访问一个节点时，令当前访问的节点为 curr，将 prev 的左子节点设为 null 以及将 prev 的右子节点设为 curr，然后将 curr 赋值给 prev
    # 初始时 prev 为 null，只有在 prev 不为 null 时才能对 prev 的左右子节点进行更新
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 寻找前驱节点
    # 前序遍历过程中需要使用栈存储节点
    # 该节点的左子树中最后一个被访问的节点是左子树中的最右边的节点，也是该节点的前驱节点。因此，问题转化成寻找当前节点的前驱节点。
    # 对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点，将当前节点的右子节点赋给前驱节点的右子节点，然后将当前节点的左子节点赋给当前节点的右子节点，并将当前节点的左子节点设为空。对当前节点处理结束后，继续处理链表中的下一个节点，直到所有节点都处理结束。
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。