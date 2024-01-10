# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack, root_stack, val_stack = [], [], []

        while stack or root:
            while root:
                stack.append(root)
                val_stack.append(root.val)
                root = root.left

            root = stack.pop()
            root_stack.append(root)

            root = root.right

        val_stack.sort()
        nodes_swap = []
        for i in range(len(val_stack)):
            if len(nodes_swap) == 2:
                break
            if root_stack[i].val != val_stack[i]:
                nodes_swap.append(root_stack[i])

        nodes_swap[0].val, nodes_swap[1].val = nodes_swap[1].val, nodes_swap[0].val

    # 显示中序遍历
    # 错误地交换 -> 破坏了值序列的递增性
    # 整个值序列中不满足条件的位置或者有两个，或者有一个
    # 如果有两个，我们记为 i 和 j -> 对应被错误交换的节点即为 ai 对应的节点和 aj+1
    # 如果有一个，我们记为 i -> 对应被错误交换的节点即为 ai 对应的节点和 ai+1
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(root, nums):
            if root == None:
                return

            inorder(root.left, nums)
            nums.append(root.val)
            inorder(root.right, nums)

        def findTwoSwapped(nums):
            n = len(nums)
            index1, index2 = -1, -1

            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    index2 = i + 1
                    if index1 == -1:
                        index1 = i
                    else:
                        break

            x, y = nums[index1], nums[index2]
            return x, y

        def recover(r, cnt, x, y):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    cnt -= 1
                    if cnt == 0:
                        return
                recover(r.left, cnt, x, y)
                recover(r.right, cnt, x, y)

        nums = []
        inorder(root, nums)
        x, y = findTwoSwapped(nums)
        recover(root, 2, x, y)

    # 隐式中序遍历
    # 只关心中序遍历的值序列中每个相邻的位置的大小关系是否满足条件，错误交换后最多两个位置不满足条件 -> 在中序遍历的过程我们只需要维护当前中序遍历到的最后一个节点 pred, 然后在遍历到下一个节点的时候，看两个节点的值是否满足前者小于后者, 找到两次以后就可以终止遍历
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stk = []
        x, y, pred = None, None, None

        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()

            if pred and root.val < pred.val:
                y = root
                if x == None:
                    x = pred
                else:
                    break

            pred = root
            root = root.right

        x.val, y.val = y.val, x.val

    # Morris中序遍历
    # 将非递归的中序遍历空间复杂度降为 O(1)
    # 如果 x 无左孩子，则访问 x 的右孩子
    # 如果 x 有左孩子，则找到 x 左子树上最右的节点，记为 predecessor
    # 如果 predecessor 的右孩子为空，则将其右孩子指向 x，然后访问 x 的左孩子
    # 如果 predecessor 的右孩子不为空，则此时其右孩子指向 x，说明我们已经遍历完 x 的左子树，将 predecessor 的右孩子置空，然后访问 x 的右孩子
    # 重复上述操作，直至访问完整棵树
    # 将当前节点左子树中最右边的节点指向它，这样在左子树遍历完成后我们通过这个指向走回了 x -> 能再通过这个知晓我们已经遍历完成了左子树，而不用再通过栈来维护，省去了栈的空间复杂度
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        x, y, pred, predecessor = None, None, None, None

        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                if predecessor.right == None:
                    predecessor.right = root
                    root = root.left
                else:
                    if pred and root.val < pred.val:
                        y = root
                        if x == None:
                            x = pred

                    pred = root
                    predecessor.right = None
                    root = root.right

            else:
                if pred and root.val < pred.val:
                    y = root
                    if x == None:
                        x = pred

                pred = root
                root = root.right

        x.val, y.val = y.val, x.val
