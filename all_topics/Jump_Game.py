class Solution:
    # 166/172
    # def canJump(self, nums: List[int]) -> bool:
    #     def check(pos, nums, seen):
    #         # print(len(nums))
    #         cur_nums_len = len(nums)
    #         # print(nums[0], nums_len)
    #         if nums[0] >= cur_nums_len - 1:
    #             # print(nums, "true 1")
    #             return True
    #         if nums[0] == 0 and cur_nums_len > 1:
    #             # print("false 1")
    #             return False

    #         # seen = []
    #         end_pos = min(nums[0] + 1, cur_nums_len)
    #         # print(end_pos)
    #         # for j in range(end_pos - 1, 0, -1):
    #         for j in range(1, end_pos):
    #             # print(nums, j, nums[j], seen, nums_len)
    #             if len(seen) == nums_len:
    #                 # print("false 2")
    #                 return False
    #             if j + pos in seen:
    #                 # print(seen)
    #                 continue
    #             if nums[j] == 0 and j < cur_nums_len - j - 1:
    #                 # return False
    #                 seen.append(j + pos)
    #                 continue
    #             if nums[j] >= cur_nums_len - j - 1:
    #                 # print(nums, nums[j], "true 2")
    #                 return True

    #             # if check(j + pos, nums[j:], seen):
    #             #     # print(nums[j: ], "true 3")
    #             #     return True
    #             # else:
    #             #     seen.append(j + pos)
    #             return check(j + pos, nums[j:], seen)

    #         # print(nums, "false final")
    #         return False

    #     seen = []
    #     nums_len = len(nums)
    #     return check(0, nums, seen)

    # 对于每一个可以到达的位置 x，它使得 x+1,x+2,⋯ ,x+nums[x] 这些连续的位置都可以到达
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/jump-game/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。