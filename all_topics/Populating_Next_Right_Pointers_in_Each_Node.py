"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # not work
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or (not root.left and not root.right):
            return root

        stack = [root]

        while stack:
            cur_stk_size = len(stack)
            # print(cur_stk_size)
            for i in range(cur_stk_size):
                cur = stack.pop(0)
                if i != cur_stk_size - 1:
                    # print(cur.val)
                    # cur.next = Node(stack[0].val)
                    # !!!!!!!!
                    cur.next = stack[0]
                    # print(cur.next.val)

                if cur.left and cur.right:
                    stack.append(cur.left)
                    stack.append(cur.right)

        return root

    # 层次遍历
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])

        # 外层的 while 循环迭代的是层数
        while Q:
            # 记录当前队列大小
            size = len(Q)

            # 遍历这一层的所有节点
            for i in range(size):

                # 从队首取出元素
                node = Q.popleft()

                # 连接
                if i < size - 1:
                    node.next = Q[0]

                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # 返回根节点
        return root

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/solutions/446938/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 使用已建立的 next 指针
    # 两种类型的 next
    # 连接同一个父节点的两个子节点 -> node.left.next = node.right
    # 不同父亲的子节点之间建立连接 -> 如果每个节点有指向父节点的指针，可以通过该指针找到 next 节点。如果不存在:
    # 连接的是第一个父节点的右孩子和第二父节点的左孩子 -> 直接通过第一个父节点的 next 指针找到第二个父节点 -> node.right.next = node.next.left
    # 第 N 层节点之间建立 next 指针后，再建立第 N+1 层节点的 next 指针
    # 通过 next 指针访问同一层的所有节点
    # 可以使用第 N 层的 next 指针，为第 N+1 层节点建立 next 指针
    # 从根节点开始，由于第 0 层只有一个节点，所以不需要连接，直接为第 1 层节点建立 next 指针即可
    # 遍历某一层的节点时，这层节点的 next 指针已经建立。因此我们只需要知道这一层的最左节点，就可以按照链表方式遍历，不需要使用队列
    # 如果当前最左节点的左孩子不存在，说明已经到达该树的最后一层，完成了所有节点的连接。
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # 从根节点开始
        leftmost = root

        while leftmost.left:
            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            head = leftmost
            while head:
                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left

                # 指针向后移动
                head = head.next

            # 去下一层的最左的节点
            leftmost = leftmost.left

        return root

    # 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/solutions/446938/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。