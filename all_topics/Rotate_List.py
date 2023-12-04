# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head == None or head.next == None:
            return head

        len_ls = 0

        dummy = head
        temp_left = res = ListNode(0)
        while dummy:
            dummy = dummy.next
            len_ls += 1

        shift = (len_ls - k) % len_ls

        i = 0
        while i < shift:
            temp_left.next = ListNode(head.val)
            temp_left = temp_left.next

            head = head.next
            i += 1

        temp_right = res2 = head
        i = 0
        while temp_right.next:
            temp_right = temp_right.next
            i += 1

        temp_right.next = res.next

        return res2

    # 先连再断
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        if (add := n - k % n) == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        print(ret)
        return ret

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/rotate-list/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。