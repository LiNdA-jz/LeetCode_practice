# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 超出时间限制
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return head

    #     dummy = ListNode(0)
    #     dummy.next = head

    #     last_sorted = head
    #     curr = head.next

    #     while curr:
    #         if last_sorted.val <= curr.val:
    #             last_sorted = last_sorted.next

    #         else:
    #             prev = dummy

    #             while prev.next.val <= curr.val:
    #                 prev = prev.next

    #             last_sorted.next = curr.next
    #             curr.next = prev.next
    #             prev.next = curr

    #         curr = last_sorted.next

    #     return dummy.next

    # 插入排序的时间复杂度是 O(n^2)
    # 题目的进阶问题要求达到 O(nlog⁡n) 的时间复杂度和 O(1) 的空间复杂度，时间复杂度是 O(nlog⁡n) 的排序算法包括归并排序、堆排序和快速排序（快速排序的最差时间复杂度是 O(n^2)
    # 归并排序基于分治算法。最容易想到的实现方式是自顶向下的递归实现，考虑到递归调用的栈空间，自顶向下归并排序的空间复杂度是 O(log⁡n)。如果要达到 O(1) 的空间复杂度，则需要使用自底向上的实现方式
    # 自顶向下归并排序
    # 找到链表的中点, 将链表拆分成两个子链表
    # 对两个子链表分别排序
    # 将两个排序后的子链表合并
    # 递归的终止条件是链表的节点个数小于或等于 1，即当链表为空或者链表只包含 1 个节点时
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)

    # # 作者：力扣官方题解
    # # 链接：https://leetcode.cn/problems/sort-list/solutions/492301/pai-xu-lian-biao-by-leetcode-solution/
    # # 来源：力扣（LeetCode）
    # # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 自底向上归并排序
    # 首先求得链表的长度, 然后将链表拆分成子链表进行合并
    # 用 subLength 表示每次需要排序的子链表的长度，初始时 subLength=1
    # 每次将链表拆分成若干个长度为 subLength 的子链表（最后一个子链表的长度可以小于 subLength，按照每两个子链表一组进行合并，合并后即可得到若干个长度为 subLength×2 的有序子链表（最后一个子链表的长度可以小于 subLength×2）
    # 将 subLength 的值加倍，重复第 2 步, 对更长的有序子链表进行合并操作, 直到有序子链表的长度大于或等于 length
    # 每个长度为 1 的子链表都是有序的
    # 如果每个长度为 subLength 的子链表已经有序，合并两个长度为 subLength 的有序子链表，得到长度为 subLength×2 的子链表，一定也是有序的
    # 当最后一个子链表的长度小于 subLength 时，该子链表也是有序的
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1

        return dummyHead.next

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/sort-list/solutions/492301/pai-xu-lian-biao-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。