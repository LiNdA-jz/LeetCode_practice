# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # not work
    # def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # print(head)
    #     temp = res = ListNode()
    #     res_ls = []

    #     while head:
    #         if len(res_ls) == 0:
    #             temp = head
    #             res_ls.append(head)
    #         else:
    #             cur_val = head.val

    #             for i in range(len(res_ls)):
    #                 if res_ls[i].val < cur_val:
    #                     continue
    #                 res_ls = res_ls[:i] + [head] + res_ls[i:]
    #                 break
    #         head = head.next

    #     # print(res_ls)
    #     for i in range(len(res_ls) - 1):
    #         res_ls[i].next = ListNode(res_ls[i + 1].val)

    #     res_ls[-1].next = None

    #     print(res_ls)
    #     print(temp, res.next)
    #     return res.next

    # 从前往后找插入点
    # 对于链表而言，插入元素时只要更新相邻节点的指针即可
    # 首先判断给定的链表是否为空，若为空，则不需要进行排序，直接返回。
    # 创建哑节点 dummyHead，令 dummyHead.next = head。引入哑节点是为了便于在 head 节点之前插入节点。
    # 维护 lastSorted 为链表的已排序部分的最后一个节点，初始时 lastSorted = head。
    # 维护 curr 为待插入的元素，初始时 curr = head.next。
    # 比较 lastSorted 和 curr 的节点值。
    # 若 lastSorted.val <= curr.val，说明 curr 应该位于 lastSorted 之后，将 lastSorted 后移一位，curr 变成新的 lastSorted。
    # 否则，从链表的头节点开始往后遍历链表中的节点，寻找插入 curr 的位置。令 prev 为插入 curr 的位置的前一个节点，进行如下操作，完成对 curr 的插入
    # lastSorted.next = curr.next
    # curr.next = prev.next
    # prev.next = curr
    # 令 curr = lastSorted.next，此时 curr 为下一个待插入的元素。
    # 重复第 5 步和第 6 步，直到 curr 变成空，排序结束。
    # 返回 dummyHead.next，为排序后的链表的头节点。
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next

        return dummyHead.next

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/insertion-sort-list/solutions/491124/dui-lian-biao-jin-xing-cha-ru-pai-xu-by-leetcode-s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。