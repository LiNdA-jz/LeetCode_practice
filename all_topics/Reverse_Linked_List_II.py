# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        sub_set = []
        dummy = final_set = ListNode()

        while idx < left:
            final_set.next = ListNode(head.val)
            head = head.next
            final_set = final_set.next
            idx += 1

        while idx <= right:
            sub_set.append(head.val)
            head = head.next
            idx += 1

        sub_n = len(sub_set)
        for i in range(sub_n - 1, -1, -1):
            final_set.next = ListNode(sub_set[i])
            final_set = final_set.next

        final_set.next = head

        return dummy.next

    # 链表的操作问题，一般而言面试（机试）的时候不允许我们修改节点的值，而只能修改节点的指向操作。
    # 穿针引线
    # 先将待反转的区域反转
    # 把 pre 的 next 指针指向反转以后的链表头节点，把反转以后的链表的尾节点的 next 指针指向 succ
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_linked_list(head: ListNode):
            # 也可以使用递归反转一个链表
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        # 因为头节点有可能发生变化，使用虚拟头节点可以避免复杂的分类讨论
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        # 第 1 步：从虚拟头节点走 left - 1 步，来到 left 节点的前一个节点
        # 建议写在 for 循环里，语义清晰
        for _ in range(left - 1):
            pre = pre.next

        # 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next
        # 第 3 步：切断出一个子链表（截取链表）
        left_node = pre.next
        curr = right_node.next

        # 注意：切断链接
        pre.next = None
        right_node.next = None

        # 第 4 步：同第 206 题，反转链表的子区间
        reverse_linked_list(left_node)
        # 第 5 步：接回到原来的链表中
        pre.next = right_node
        left_node.next = curr
        return dummy_node.next

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/reverse-linked-list-ii/solutions/634701/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 一次遍历「穿针引线」反转链表（头插法）
    # 使用三个指针变量 pre、curr、next
        # curr：指向待反转区域的第一个节点 left
        # next：永远指向 curr 的下一个节点，循环过程中，curr 变化以后 next 会变化
        # pre：永远指向待反转区域的第一个节点 left 的前一个节点，在循环过程中不变
    # 先将 curr 的下一个节点记录为 next
    # 把 curr 的下一个节点指向 next 的下一个节点
    # 把 next 的下一个节点指向 pre 的下一个节点
    # 把 pre 的下一个节点指向 next
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/reverse-linked-list-ii/solutions/634701/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。