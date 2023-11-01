class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time Limit Exceeded
        # n = len(height)
        # dp = [[0]*n]*n
        # max_water = 0

        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if (height[i] <= height[j]):
        #             dp[i][j] = height[i] * (j-i)

        #         else:
        #             dp[i][j] = height[j] * (j-i)

        #         max_water = max(max_water, dp[i][j])

        # return max_water

        left, right, answer = 0, len(height) - 1, 0
        while left <= right:
            area = min(height[right], height[left]) * (right - left)
            answer = max(answer, area)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return answer

    # practice on 01/11/2023
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 2:
            return height[0] if height[0] <= height[1] else height[1]

        max_vol = 0

        l = 0
        r = len(height) - 1

        while l < r:
            if height[l] <= height[r]:
                cur_vol = height[l] * (r - l)
                max_vol = max(max_vol, cur_vol)
                l += 1
            else:
                cur_vol = height[r] * (r - l)
                max_vol = max(max_vol, cur_vol)
                r -= 1

            # print(l," ", r, " ", max_vol)

        return max_vol