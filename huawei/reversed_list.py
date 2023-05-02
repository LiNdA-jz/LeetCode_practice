# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # res_ls = []

        # while head:
        #     res_ls.append(head.val)
        #     head = head.next

        # # print(res_ls)
        # res = cur = ListNode()
        # while res_ls:
        #     cur.next = ListNode(res_ls.pop(-1))
        #     # print(res_ls)
        #     # print(res.next)
        #     cur = cur.next

        # return res.next

        # 在遍历链表时，将当前节点的 next 指针改为指向前一个节点。由于节点没有引用其前一个节点，因此必须事先存储其前一个节点。
        # 在更改引用之前，还需要存储后一个节点。最后返回新的头引用。

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/UHnkqh/solution/fan-zhuan-lian-biao-by-leetcode-solution-34oi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        pre, cur = None, head
        while cur:
            nxt = cur.next  # 记录当前节点的下一个节点
            cur.next = pre  # 然后将当前节点指向pre
            pre = cur  # pre和cur节点都前进一位
            cur = nxt
        return pre