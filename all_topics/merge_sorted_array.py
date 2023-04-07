class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # j = 0
        # num_count = m
        # for i in nums2[:n]:
        #     print(i, j)
        #     while (j<n+m):
        #         if (i >= nums1[j]) and (j<num_count):
        #             j += 1
        #         else:
        #             nums1.insert(j, i)
        #             num_count += 1
        #             nums1.pop()
        #             print(nums1)
        #             break

        # Initialize nums1's index
        i = m - 1
        # Initialize nums2's index
        j = n - 1
        # Initialize a variable k to store the last index of the 1st array...
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1