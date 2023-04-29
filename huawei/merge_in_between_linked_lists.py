# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # not work
        # input:
        # [0,3,2,1,4,5]
        # 3
        # 4
        # [1000000,1000001,1000002]
        # got:
        # [0,1000000,1000001,1000002,5]
        # expect:
        # [0,3,2,1000000,1000001,1000002,5]?
        cur = res = ListNode()
        a_count = 0
        while a_count != a:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
            a_count += 1

        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next

        b_count = a
        while b_count != b:
            list1 = list1.next
            b_count += 1

        cur.next = list1.next
        while list1:
            cur = cur.next
            cur = list1.next
            list1 = list1.next

        # cur = list1.next
        # print(res)
        return res.next

#         preA = list1
#         for _ in range(a - 1):
#             preA = preA.next
#         preB = preA
#         for _ in range(b - a + 2):
#             preB = preB.next
#         preA.next = list2
#         while list2.next:
#             list2 = list2.next
#         list2.next = preB
#         return list1

# # 作者：LeetCode-Solution
# # 链接：https://leetcode.cn/problems/merge-in-between-linked-lists/solution/he-bing-liang-ge-lian-biao-by-leetcode-s-alt8/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。