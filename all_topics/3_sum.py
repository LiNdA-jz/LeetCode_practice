class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # not work
        # l, r = 0, len(nums) - 1

        # zero_sum_ls = []

        # while l < r:

        #     diff = 0 - (nums[l] + nums[r])
        #     # print(l, r)
        #     for i in range(l+1, r):
        #         if diff == nums[i]:
        #             if [nums[i], nums[l], nums[r]] not in zero_sum_ls:
        #                 # print([nums[i], nums[l], nums[r]])
        #                 zero_sum_ls.append([nums[i], nums[l], nums[r]])

        #     if abs(nums[l]) > abs(nums[r]):
        #         l += 1
        #     else:
        #         r -= 1

        # return zero_sum_ls

        # res = set()

        # #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        # n, p, z = [], [], []
        # for num in nums:
        #     if num > 0:
        #         p.append(num)
        #     elif num < 0:
        #         n.append(num)
        #     else:
        #         z.append(num)

        # #2. Create a separate set for negatives and positives for O(1) look-up times
        # N, P = set(n), set(p)

        # #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        # #   i.e. (-3, 0, 3) = 0
        # if z:
        #     for num in P:
        #         if -1*num in N:
        #             res.add((-1*num, 0, num))

        # #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        # if len(z) >= 3:
        #     res.add((0,0,0))

        # #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        # #   exists in the positive number set
        # for i in range(len(n)):
        #     for j in range(i+1,len(n)):
        #         target = -1*(n[i]+n[j])
        #         if target in P:
        #             res.add(tuple(sorted([n[i],n[j],target])))

        # #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        # #   exists in the negative number set
        # for i in range(len(p)):
        #     for j in range(i+1,len(p)):
        #         target = -1*(p[i]+p[j])
        #         if target in N:
        #             res.add(tuple(sorted([p[i],p[j],target])))

        # return res

        nums.sort()  # sorting cause we need to avoid duplicates, with this duplicates will be near to each other
        l = []
        for i in range(len(nums)):  # this loop will help to fix the one number i.e, i
            if i > 0 and nums[i - 1] == nums[i]:  # skipping if we found the duplicate of i
                continue

            # NOW FOLLOWING THE RULE OF TWO POINTERS AFTER FIXING THE ONE VALUE (i)
            j = i + 1  # taking j pointer larger than i (as said in ques)
            k = len(nums) - 1  # taking k pointer from last
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:  # if sum s is greater than 0(target) means the larger value(from right as nums is sorted i.e, k at right)
                    # is taken and it is not able to sum up to the target
                    k -= 1  # so take value less than previous
                elif s < 0:  # if sum s is less than 0(target) means the shorter value(from left as nums is sorted i.e, j at left)
                    # is taken and it is not able to sum up to the target
                    j += 1  # so take value greater than previous
                else:
                    l.append([nums[i], nums[j], nums[k]])  # if sum s found equal to the target (0)
                    j += 1
                    while nums[j - 1] == nums[
                        j] and j < k:  # skipping if we found the duplicate of j and we dont need to check
                        # the duplicate of k cause it will automatically skip the duplicate by the adjustment of i and j
                        j += 1
        return l