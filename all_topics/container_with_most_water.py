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