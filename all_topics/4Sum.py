class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res_ls = []

        def twoSum(remain_nums, remain_tgt):
            two_l, two_r = 0, len(remain_nums) - 1
            remain_res_ls = []

            while two_l < two_r:
                cur_sum = remain_nums[two_l] + remain_nums[two_r]

                if cur_sum < remain_tgt:
                    two_l += 1
                elif cur_sum > remain_tgt:
                    two_r -= 1
                else:
                    remain_res_ls.append([remain_nums[two_l], remain_nums[two_r]])

                    two_l += 1
                    while two_l < two_r and remain_nums[two_l - 1] == remain_nums[two_l]:
                        two_l += 1

            return remain_res_ls

        for l in range(len(nums)):
            r = len(nums) - 1

            remain_ls = []

            while l < r:
                two_sum = nums[l] + nums[r]
                remain_sum = target - two_sum
                remain_ls = twoSum(nums[l + 1:r], remain_sum)

                if remain_ls:
                    for remain in remain_ls:
                        if [nums[l]] + remain + [nums[r]] not in res_ls:
                            res_ls.append([nums[l]] + remain + [nums[r]])

                r -= 1

        return res_ls

        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            quadruplets = list()
            if not nums or len(nums) < 4:
                return quadruplets

            nums.sort()
            length = len(nums)
            for i in range(length - 3):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                # smallest combination larger than tgt -> impossible
                if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                    break
                # i too small
                if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                    continue
                # similar to i
                for j in range(i + 1, length - 2):
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue
                    if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                        break
                    if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                        continue
                    left, right = j + 1, length - 1
                    while left < right:
                        total = nums[i] + nums[j] + nums[left] + nums[right]
                        if total == target:
                            quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                            while left < right and nums[left] == nums[left + 1]:
                                left += 1
                            left += 1
                            while left < right and nums[right] == nums[right - 1]:
                                right -= 1
                            right -= 1
                        elif total < target:
                            left += 1
                        else:
                            right -= 1

            return quadruplets

    # 作者：力扣官方题解
    # 链接：https: // leetcode.cn / problems / 4
    # sum /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。