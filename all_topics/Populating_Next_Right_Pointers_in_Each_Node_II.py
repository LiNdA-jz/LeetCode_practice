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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        stk = [root]

        while stk:
            stk_size = len(stk)

            for i in range(stk_size):
                cur = stk.pop(0)
                if i != stk_size - 1:
                    cur.next = stk[0]
                if cur.left:
                    stk.append(cur.left)
                if cur.right:
                    stk.append(cur.right)

        return root

    # 层次遍历
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        queue = deque([root])
        while queue:
            n = len(queue)
            last = None
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if last:
                    last.next = node
                last = node
        return root

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/solutions/429828/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-15/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 使用已建立的 next 指针
    # 在上一层为下一层建立 next 指针
    # 每次只要知道下一层的最左边的节点
    # 如果第 i 层节点之间已经建立 next 指针，就可以通过 next 指针访问该层的所有节点，同时对于每个第 i 层的节点，我们又可以通过它的 left 和 right 指针知道其第 i+1 层的孩子节点是什么，所以遍历过程中就能够按顺序为第 i+1 层节点建立 next 指针
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        start = root

        while start:
            self.last = None
            self.nextStart = None
            p = start

            while p:
                if p.left:
                    self.handle(p.left)
                if p.right:
                    self.handle(p.right)
                p = p.next

            start = self.nextStart

        return root

    def handle(self, p):
        if self.last:
            self.last.next = p
        if not self.nextStart:
            self.nextStart = p
        self.last = p

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/solutions/429828/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-15/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。