class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums)==1 or len(nums)==0):
            return nums
        
        zero = nums.count(0)
        

        for i in range(zero):
            nums.remove(0)
            nums.append(0)


        # swap
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

        # faster
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1


        # c++
        # Space Complexity : O(n)
        # Time Complexity: O(n)
        # void moveZeroes(vector<int>& nums) {
        #     int n = nums.size();

        #     // Count the zeroes
        #     int numZeroes = 0;
        #     for (int i = 0; i < n; i++) {
        #         numZeroes += (nums[i] == 0);
        #     }

        #     // Make all the non-zero elements retain their original order.
        #     vector<int> ans;
        #     for (int i = 0; i < n; i++) {
        #         if (nums[i] != 0) {
        #             ans.push_back(nums[i]);
        #         }
        #     }

        #     // Move all zeroes to the end
        #     while (numZeroes--) {
        #         ans.push_back(0);
        #     }

        #     // Combine the result
        #     for (int i = 0; i < n; i++) {
        #         nums[i] = ans[i];
        #     }
        # }


        # Space Complexity : O(1)
        # Time Complexity: O(n)
        # void moveZeroes(vector<int>& nums) {
        #     int lastNonZeroFoundAt = 0;
        #     // If the current element is not 0, then we need to
        #     // append it just in front of last non 0 element we found. 
        #     for (int i = 0; i < nums.size(); i++) {
        #         if (nums[i] != 0) {
        #             nums[lastNonZeroFoundAt++] = nums[i];
        #         }
        #     }
        #     // After we have finished processing new elements,
        #     // all the non-zero elements are already at beginning of array.
        #     // We just need to fill remaining array with 0's.
        #     for (int i = lastNonZeroFoundAt; i < nums.size(); i++) {
        #         nums[i] = 0;
        #     }
        # }


        # Space Complexity : O(1)
        # Time Complexity: O(n)
        # void moveZeroes(vector<int>& nums) {
        #     for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
        #         if (nums[cur] != 0) {
        #             swap(nums[lastNonZeroFoundAt++], nums[cur]);
        #         }
        #     }
        # }