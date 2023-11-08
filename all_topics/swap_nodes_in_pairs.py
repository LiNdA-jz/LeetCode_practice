# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d1 = d = ListNode(0)
        d.next = head

        while d.next and d.next.next:
            p = d.next
            q = d.next.next

            d.next, p.next, q.next = q, q.next, p

            d = p
            # print(d.next)
            # print(d1.next)
        return d1.next

# (0->)1->2->3->4
#  d   p  q

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = cur = ListNode()
        # print(dummy)

        while head:
            if head.next:
                dummy.next = ListNode(head.next.val)
                dummy.next.next = ListNode(head.val)
                head = head.next.next
                dummy = dummy.next.next
            else:
                dummy.next = ListNode(head.val)
                return cur.next

            print(dummy)

        return cur.next

    # better performance (memory)
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/swap-nodes-in-pairs/description/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。