"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # not work
    # def __init__(self):
    #     self.visited = {}

    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     if not head or not head.next:
    #         return head

    #     if head in self.visited:
    #         return self.visited[head]

    #     new_node = Node(head.val, head.next, head.random)

    #     self.visited[head] = new_node

    #     if head.next:
    #         new_node.next = self.copyRandomList(head.next)

    #     return new_node

    # 回溯 + 哈希表
    # 如果是普通链表，我们可以直接按照遍历的顺序创建链表节点
    # 而本题中因为随机指针的存在，当我们拷贝节点时，「当前节点的随机指针指向的节点」可能还没创建
    # 可行方案是，利用回溯的方式，让每个节点的拷贝操作相互独立
    # 对于当前节点，我们首先要进行拷贝，然后我们进行「当前节点的后继节点」和「当前节点的随机指针指向的节点」拷贝
    def __init__(self):
        self.cacheNode = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        if head not in self.cacheNode:
            new_node = Node(head.val)
            self.cacheNode[head] = new_node
            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)

        return self.cacheNode[head]


    # 迭代 + 节点拆分
    # 方法一需要使用哈希表记录每一个节点对应新节点的创建情况
    # 将该链表中每一个节点拆分为两个相连的节点
        # 例如对于链表 A→B→C，我们可以将其拆分为 A→A′→B→B′→C→C'
        # 可以直接找到每一个拷贝节点 S′ 的随机指针应当指向的节点, 即为其原节点 S 的随机指针指向的节点 T 的后继节点 T′
        # 原节点的随机指针可能为空，我们需要特别判断这种情况
    # 将这个链表按照原节点与拷贝节点的种类进行拆分即可，只需要遍历一次
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        node = head
        while node:
            new_node = Node(node.val)
            new_node.next = node.next
            node.next = new_node
            node = node.next.next

        node = head
        while node:
            new_node = node.next
            new_node.random = (node.random.next) if node.random else None
            node = node.next.next

        new_head = head.next
        node = head
        while node:
            new_node = node.next
            node.next = node.next.next
            new_node.next = new_node.next.next if new_node.next else None
            node = node.next

        return new_head