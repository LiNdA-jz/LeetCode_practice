class Solution:
    # not work
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     if len(nums) == 0 or target not in nums:
    #         return [-1, -1]

    #     l, r = 0, len(nums) - 1
    #     res = [r, l]

    #     while l < r:
    #         mid = (l + r) // 2
    #         print(l, " ", r, " ", mid)

    #         if target == nums[l]:
    #             res[0] = l
    #             print(res[0])
    #             break
    #         if target == nums[r]:
    #             res[1] = r
    #             print(res[1])
    #             break

    #         if target > nums[mid]:
    #             r -= 1
    #             l = mid + 1
    #         elif target < nums[mid]:
    #             l += 1
    #             r = mid
    #         else:
    #             for i in range(mid + 1):
    #                 if nums[i] == target:
    #                     print(i)
    #                     res[0] = i
    #                     break
    #             for i in range(len(nums) - 1, mid - 1, -1):
    #                 if nums[i] == target:
    #                     print(i)
    #                     res[1] = i
    #                     break

    #             return res

    #     print(res)
    #     if l > r:
    #         return [-1, -1]
    #     else:
    #         if res[0] == -1:
    #             for i in range(res[1] + 1):
    #                 if nums[i] == target:
    #                     print(i)
    #                     res[0] = i
    #                     return res
    #         else:
    #             for i in range(len(nums) - 1, res[0] - 1, -1):
    #                 if nums[i] == target:
    #                     print(i)
    #                     res[1] = i
    #                     return res

    # 二分查找
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, lower):
            l, r, ans = 0, len(nums) - 1, len(nums)

            while l <= r:
                mid = (l + r) // 2

                if (nums[mid] > target) or (lower and nums[mid] >= target):
                    r = mid - 1
                    ans = mid
                else:
                    l = mid + 1

            return ans

        l_idx = binarySearch(nums, target, True)
        r_idx = binarySearch(nums, target, False) - 1

        if (l_idx <= r_idx and r_idx < len(nums) and nums[l_idx] == target and nums[r_idx] == target):
            return [l_idx, r_idx]
        return [-1, -1]