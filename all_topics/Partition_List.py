# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        gth = temp = ListNode(0)
        dummy = ListNode(0, head)

        cur = dummy
        while cur.next:
            if cur.next.val >= x:
                while cur.next and cur.next.val >= x:
                    temp.next = ListNode(cur.next.val)
                    temp = temp.next
                    cur.next = cur.next.next
            else:
                cur = cur.next

        # print(gth)
        cur.next = gth.next

        return dummy.next

    # 模拟
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        small_head = small
        large = ListNode(0)
        large_head = large

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None
        small.next = large_head.next

        return small_head.next