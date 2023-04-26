class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # not work
        # # print(list(reversed(sorted(nums))))

        # positive = []
        # negative = []

        # for i in nums:
        #     if i <= 0:
        #         negative.append(i)
        #     else:
        #         positive.append(i)

        # positive = list(reversed(sorted(positive)))
        # negative = list(reversed(sorted(negative)))

        # # print(positive, negative)

        # res = positive + [sum(positive)]
        # total_sum = sum(nums)
        # if total_sum > 0:
        #     res.append(total_sum)
        #     res = list(reversed(sorted(res)))
        #     appended = True
        # else:
        #     appended = False
        # # print(res)

        # while len(res) < k:
        #     if len(positive) > 0:
        #         positive.pop(0)
        #         res.append(sum(positive))
        #         res = list(reversed(sorted(res)))
        #         print(res)
        #     elif len(negative) > 0:
        #         if not appended:
        #             if total_sum >= negative[0]:
        #                 res.append(total_sum)
        #                 appended = True
        #         if len(res) > 0:
        #             res.append(res[-1] + negative[0])
        #         else:
        #             res.append(negative[0])
        #         negative.pop(0)

        # print(res)
        # return res[-1]


        # 1. max: sum of all non-negative
        # 2. minus (k-1) min subsequence from max
        tot = 0
        for i, x in enumerate(nums):
            if x >= 0: tot += x
            else: nums[i] = -x
        nums.sort()
        # print(nums)
        # 大顶堆
        h = [(0, 0)]
        while k > 1:
            k -= 1
            # print("cur: ", h)
            s, i = heappop(h)
            if i < len(nums):
                # 排序针对元组中第一个元素
                heappush(h, (s + nums[i], i + 1))  # 保留 nums[i-1]
                # print("push1: ", h, i)
                if i:
                    heappush(h, (s + nums[i] - nums[i - 1], i + 1))  # 不保留 nums[i-1]
                    # print("push2: ", h)
            print(h)
        return tot - h[0][0]

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/find-the-k-sum-of-an-array/solution/zhuan-huan-dui-by-endlesscheng-8yiq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。