class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # not work
        neg_sq = []
        print(len(nums))
        for i in range(len(nums)):
            if (nums[i]<0):
                neg_sq.append(nums[i]**2)
                nums.pop(i)

        sq = [num**2 for num in nums]
        l, r = 0, len(sq)-1
        for neg_num in neg_sq:
            while (l < r):
                mid = l + (r-l)//2
                if (neg_num==sq[mid]):
                    sq.insert(mid,neg_num)
                    l = mid + 1
                elif (neg_num < sq[mid]):
                    r = mid
                else:
                    l = mid + 1
            sq.insert(l+1,neg_num) if (neg_num>nums[l]) else sq.insert(l,neg_num)

        return sq

        # deque
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)


        # without deque
        answer = [0] * len(A)
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer