# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # not work
        # name 'mergeTwoLists' is not defined
        # mergeTwoLists(self, list1, list2)
        # if (not list1):
        #     return list2
        # elif (not list2):
        #     return list1
        # else:
        #     if (list1.val > list2.val):
        #         temp = list1.val
        #         list1.val = list2.val
        #         list1.next = temp
        #         list2.val = list2.next
        #         list2.next = list2.next.next
        #     mergeTwoLists(self, list1, list2)

        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next