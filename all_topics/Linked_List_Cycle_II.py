# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.visited = []

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            # print("no cycle")
            return None

        if head not in self.visited:
            self.visited.append(head)
            return self.detectCycle(head.next)
        else:
            return head

        # print(self.visited)
        if not self.visited:
            return None

    # 哈希表
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = []

        while head:
            if head in visited:
                return head
            visited.append(head)
            head = head.next

        return None

    # 快慢指针
    # slow 指针每次向后移动一个位置，而 fast 指针向后移动两个位置
    # 如果链表中存在环，则 fast 指针最终将再次与 slow 指针在环中相遇
    # 任意时刻，fast 指针走过的距离都为 slow 指针的 2 倍
    # 设链表中环外部分的长度为 a。slow 指针进入环后，又走了 b 的距离与 fast 相遇
    # fast 指针已经走完了环的 n 圈, 因此它走过的总距离为 a+n(b+c)+b=a+(n+1)b+nc
    # a+(n+1)b+nc=2(a+b)⟹a=c+(n−1)(b+c)
    # 从相遇点到入环点的距离加上 n−1 圈的环长，恰好等于从链表头部到入环点的距离
    # 当发现 slow 与 fast 相遇时，我们再额外使用一个指针 ptr, 起始，它指向链表头部；随后，它和 slow 每次向后移动一个位置。最终，它们会在入环点相遇
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast:
            slow = slow.next
            if not fast.next:
                return None

            fast = fast.next.next

            if fast == slow:
                ptr = head

                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next

                return ptr

        return None