# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # not work for recursion
        # carry = 0

        # if not ((l1.next == None) and (l2.next == None)):
        #     if (l1.val + l2.val) < 10:
        #         return (l1.val + l2.val) + addTwoNumbers(l1.next, l2.next)
        #     else:
        #         carry

        # not work
        # only the last few val
        # carry = 0
        # res = ListNode()

        # while l1 or l2 or carry:
        #     if (l1.next == None) and (l2.next == None):
        #         if (l1.val + l2.val + carry) < 10:
        #             res.next = ListNode(l1.val + l2.val + carry)
        #         else:
        #             carry = (l1.val + l2.val + carry) // 10
        #             res.next = ListNode((l1.val + l2.val + carry) % 10)
        #             res.next.next = ListNode(carry)
        #         return res

        #     elif l1.next == None:
        #         if (l1.val + l2.val + carry) < 10:
        #             res.next = ListNode(l1.val + l2.val + carry)
        #         else:
        #             res.next = ListNode((l1.val + l2.val + carry) % 10)
        #             carry = (l1.val + l2.val + carry) // 10
        #         l1 = ListNode(0)
        #         l2 = l2.next

        #     elif l2.next == None:
        #         if (l1.val + l2.val + carry) < 10:
        #             res.next = ListNode(l1.val + l2.val + carry)
        #         else:
        #             res.next = ListNode((l1.val + l2.val + carry) % 10)
        #             carry = (l1.val + l2.val + carry) // 10
        #         l2 = ListNode(0)
        #         l1 = l1.next

        #     else:
        #         if (l1.val + l2.val + carry) < 10:
        #             res.next = ListNode(l1.val + l2.val + carry)
        #         else:
        #             res.next = ListNode((l1.val + l2.val + carry) % 10)
        #             carry = (l1.val + l2.val + carry) // 10
        #         l1 = l1.next
        #         l2 = l2.next

        # return res

        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            res_val = v1 + v2 + carry
            carry = res_val // 10
            res_val = res_val % 10
            cur.next = ListNode(res_val)

            # update
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next