# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # not work
        # if (headA == None) and (headB == None):
        #     if (headA.next == None) or (headB.next == None):
        #         return "No intersection"
        #     return self.getIntersectionNode(headA.next, headB.next)
        # elif (headA == None):
        #     return  self.getIntersectionNode(headA.next, headB)
        # elif (headB == None):
        #     return  self.getIntersectionNode(headA, headB.next)

        # stackA = ['A']
        # stackB = ['B']

        # while headA or headB:
        #     if headA:
        #         stackA.append(headA)
        #         headA = headA.next

        #     if headB:
        #         stackB.append(headB)
        #         headB = headB.next

        # prev = None
        # while stackA and stackB:
        #     nodeA = stackA.pop(-1)
        #     nodeB = stackB.pop(-1)

        #     if nodeA != nodeB:
        #         return prev

        #     prev = nodeA

        first_set = set()
        curr = headA

        while curr:
            first_set.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr = curr.next

        return None