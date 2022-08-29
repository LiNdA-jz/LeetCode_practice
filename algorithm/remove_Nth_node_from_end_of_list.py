# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # not work
        list_length = 0
        head_copy = head
        while (head_copy.next):
            list_length += 1
            head_copy = head_copy.next
        
        num_count = 0
        while (num_count<list_length-n+1):
            num_count += 1
            head = head.next
        
        head.next = head.next.next
        return head


        # To do that, we can simply stagger our two pointers by n nodes by giving the first pointer (fast) a head start before starting the second pointer (slow).
        # Doing this will cause slow to reach the n'th node from the end at the same time that fast reaches the end.
        # Since we will need access to the node before the target node in order to remove the target node,
        # we can use fast.next == null as our exit condition, rather than fast == null, so that we stop one node earlier.
        # This will unfortunately cause a problem when n is the same as the length of the list, which would make the first node the target node,
        # and thus make it impossible to find the node before the target node.
        # If that's the case, however, we can just return head.next without needing to stitch together the two sides of the target node.
        # Time Complexity : O(N), where, N is the number of nodes in the given list.
        # Space Complexity : O(1), since only constant space is used.
        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head

        # value shift
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

        # index and remove
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]