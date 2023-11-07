# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # more efficient
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num_ls = []

        while head:
            num_ls.append(head.val)
            head = head.next

        remove_idx = len(num_ls) - n

        num_ls.pop(remove_idx)

        res = dummy = ListNode()
        for i in range(len(num_ls)):
            dummy.next = ListNode(num_ls[i])
            dummy = dummy.next

        return res.next

        def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
            def getLength(head: ListNode) -> int:
                length = 0
                while head:
                    length += 1
                    head = head.next
                return length

            dummy = ListNode(0, head)
            length = getLength(head)
            cur = dummy
            for i in range(1, length - n + 1):
                cur = cur.next
            cur.next = cur.next.next
            return dummy.next

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。