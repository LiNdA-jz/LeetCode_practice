# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # not work
        # if head == None:
        #     return False

        # if head.next == None:
        #     return False

        # st = []
        # while head.next:
        #     if head.val in st:
        #         return True
        #     else:
        #         st.append(head.val)
        #         head = head.next

        # return head.val in st

        # keep hashmap of nodes
        nodes = {}

        while (head):
            if head.next not in nodes:
                nodes[head.next] = 1
            else:
                return True
            head = head.next

        return False

        # as per floyd's cycle detection algorithm,
        # we keep slow and fast pointers.
        # increment slow by 1 and fast by 2
        # slow = None
        # fast = head
        # while fast and fast.next:
        #     if slow == fast and slow:
        #         return slow
        #     slow = slow.next if slow else fast.next
        #     fast = fast.next.next
