# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        left = []
        while head:
            left.append(head.val)
            head = head.next

        n = len(left)
        if n == 2:
            root = TreeNode(left[0])
            root.right = TreeNode(left[1])
            return root
        elif n == 3:
            root = TreeNode(left[1])
            root.left = TreeNode(left[0])
            root.right = TreeNode(left[2])
            return root

        root = left[n // 2]
        right = left[n // 2 + 1:]
        left = left[:n // 2][::-1]

        # print(root, left, right)
        root = TreeNode(root)

        if len(left) == 1:
            root.left = TreeNode(left[0])
        else:
            list_node = cur = ListNode(left[-1])
            for i in range(n // 2 - 2, -1, -1):
                cur.next = ListNode(left[i])
                cur = cur.next
            # print(list_node)
            root.left = self.sortedListToBST(list_node)

        if len(right) == 1:
            root.right = TreeNode(right[0])
        else:
            list_node = cur = ListNode(right[0])
            for i in range(1, len(right)):
                cur.next = ListNode(right[i])
                cur = cur.next
            # print(list_node)
            root.right = self.sortedListToBST(list_node)

        return root

    # 第一步是确定根节点
    # 左子树中的节点个数与右子树中的节点个数尽可能接近
    # 分治
    # 左端点为 left，右端点 right，包含关系为「左闭右开」-> left 包含在链表中而 right 不包含在链表中
    # 如果设定「左闭右开」的关系，我们就可以直接用 (left,mid) 以及 (mid.next,right) 来表示左右子树对应的列表了
    # 初始的列表也可以用 (head,null) 方便地进行表示
    # 找出链表中位数节点的方法多种多样，其中较为简单的一种是「快慢指针法」
    # 初始时，快指针 fast 和慢指针 slow 均指向链表的左端点 left
    # 将快指针 fast 向右移动两次的同时，将慢指针 slow 向右移动一次, 直到快指针到达边界
    # 此时，慢指针对应的元素就是中位数
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root

        return buildTree(head, None)

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/solutions/378582/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 分治 + 中序遍历优化
    # 方法一的时间复杂度的瓶颈在于寻找中位数节点
    # 设当前链表的左端点编号为 left，右端点编号为 right，包含关系为「双闭」
    # 不用急着找出链表的中位数节点，而是使用一个占位节点，等到中序遍历到该节点时，再填充它的值
    # 通过计算编号范围来进行中序遍历
    # 中位数节点对应的编号为 mid=(left+right+1)/2
    # 左右子树对应的编号范围分别为 [left,mid−1] 和 [mid+1,right]
    # 如果 left>right，那么遍历到的位置对应着一个空节点，否则对应着二叉搜索树中的一个节点。
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret

        def buildTree(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root

        length = getLength(head)
        return buildTree(0, length - 1)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/solutions/378582/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。