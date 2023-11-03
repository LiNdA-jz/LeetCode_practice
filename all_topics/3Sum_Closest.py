class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = 2 * 10 ** 4
        res_sum = 0

        for l in range(len(nums)):
            mid = l + 1
            r = len(nums) - 1

            while mid < r:
                cur_sum = nums[l] + nums[mid] + nums[r]
                cur_diff = abs(target - cur_sum)
                if cur_diff < diff:
                    res_sum = cur_sum
                    diff = cur_diff

                if cur_sum < target:
                    mid += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    mid += 1
                    while nums[mid - 1] == nums[mid] and mid < r:
                        mid += 1

        return res_sum

        def threeSumClosest(self, nums: List[int], target: int) -> int:
            nums.sort()
            n = len(nums)
            best = 10 ** 7

            # 根据差值的绝对值来更新答案
            def update(cur):
                nonlocal best
                if abs(cur - target) < abs(best - target):
                    best = cur

            # 枚举 a
            for i in range(n):
                # 保证和上一次枚举的元素不相等
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                # 使用双指针枚举 b 和 c
                j, k = i + 1, n - 1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    # 如果和为 target 直接返回答案
                    if s == target:
                        return target
                    update(s)
                    if s > target:
                        # 如果和大于 target，移动 c 对应的指针
                        k0 = k - 1
                        # 移动到下一个不相等的元素
                        while j < k0 and nums[k0] == nums[k]:
                            k0 -= 1
                        k = k0
                    else:
                        # 如果和小于 target，移动 b 对应的指针
                        j0 = j + 1
                        # 移动到下一个不相等的元素
                        while j0 < k and nums[j0] == nums[j]:
                            j0 += 1
                        j = j0

            return best

    # 作者：力扣官方题解
    # 链接：https: // leetcode.cn / problems / 3
    # sum - closest /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。