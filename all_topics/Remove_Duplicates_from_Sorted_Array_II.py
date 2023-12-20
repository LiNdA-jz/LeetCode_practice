class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = nums[0]
        cur_count = 1
        n = len(nums)
        k = 1

        i = 1
        while i < n:
            if nums[i] == cur:
                cur_count += 1
                if cur_count < 3:
                    k += 1
                else:
                    while i < n and nums[i] == cur:
                        nums[i] = 10 ** 5
                        i += 1
                    if i < n:
                        cur = nums[i]
                        cur_count = 1
                        k += 1

            else:
                cur = nums[i]
                cur_count = 1
                k += 1
            i += 1
            # print(k)

        # print(k)
        nums.sort()
        return k

    # 双指针
    # 遍历数组检查每一个元素是否应该被保留，如果应该被保留，就将其移动到指定位置
    # 慢指针表示处理出的数组的长度，快指针表示已经检查过的数组的长度
    # 仅当 nums[slow−2]=nums[fast] 时，当前待检查元素 nums[fast] 不应该被保留

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        slow, fast = 2, 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        print(nums)
        return slow