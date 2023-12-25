# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = temp = ListNode()
        # print(dummy)

        while head and head.next:
            cur = head.val
            if head.next.val != cur:
                dummy.next = ListNode(cur)
                head = head.next
                cur = head.val
                dummy = dummy.next
            else:
                while head and head.val == cur:
                    head = head.next

        if head:
            dummy.next = head
        # print(temp)
        return temp.next

    # 一次遍历
    # 由于链表的头节点可能会被删除，因此我们需要额外使用一个哑节点（dummy node）指向链表的头节点
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。