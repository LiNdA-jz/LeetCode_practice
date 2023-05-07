# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # print(head)
        # even_ls = even_cur = ListNode()
        # odd_ls = odd_cur = ListNode()

        # idx_count = 1

        # while head:
        #     if idx_count % 2 == 0:
        #         # print(head.val)
        #         # print("even")
        #         even_cur.next = head
        #         # print(even_ls)
        #         even_cur = even_cur.next
        #     else:
        #         # print("odd")
        #         odd_cur.next = head
        #         odd_cur = odd_cur.next

        #     idx_count += 1
        #     head = head.next

        # even_cur.next = None
        # # print(even_ls.next)
        # # print(odd_ls.next, even_ls.next)
        # even_ls = even_ls.next
        # # print(odd_cur, odd_cur.next, even_cur, even_cur.next)
        # while even_ls:
        #     odd_cur.next = even_ls
        #     odd_cur = odd_cur.next
        #     even_ls = even_ls.next

        # return odd_ls.next

        if not head:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/odd-even-linked-list/solution/qi-ou-lian-biao-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
