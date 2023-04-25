class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1_set = set(nums1)
        # nums2_set = set(nums2)
        # res = []

        # for i in nums1_set:
        #     if i in nums2_set:
        #         res.append(i)

        # return res

        set1 = set(nums1)
        set2 = set(nums2)
        return self.set_intersection(set1, set2)

    def set_intersection(self, set1, set2):
        if len(set1) > len(set2):
            return self.set_intersection(set2, set1)
        return [x for x in set1 if x in set2]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/intersection-of-two-arrays/solution/liang-ge-shu-zu-de-jiao-ji-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。