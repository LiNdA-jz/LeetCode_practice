class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # odd = []
        # even = []
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 1:
        #         odd.append(nums[i])
        #     else:
        #         even.append(nums[i])

        # return odd + even

        return [num for num in nums if num % 2 == 1] + [num for num in nums if num % 2 == 0]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/solution/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-en35/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。