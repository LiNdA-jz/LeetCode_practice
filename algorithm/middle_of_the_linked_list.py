# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # not work
        mid = (len(head) + 1) // 2

        res = []
        while (self.next is not None):
            res.append(self.val)


        return res


        # Each time, slow go 1 steps while fast go 2 steps.
        # When fast arrives at the end, slow will arrive right in the middle.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow