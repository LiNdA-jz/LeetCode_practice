# quicksort & mergesort!!!!!!!!!
class Solution:
    def merge_sort(self, nums, l, r):
            if l == r:
                return
            mid = (l + r) // 2
            self.merge_sort(nums, l, mid)
            self.merge_sort(nums, mid + 1, r)
            tmp = []
            i, j = l, mid + 1
            while i <= mid or j <= r:
                if i > mid or (j <= r and nums[j] < nums[i]):
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            nums[l: r + 1] = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        # not work -> 超出输出限制
        # if len(nums) <= 1:
        #     return nums
        # if len(nums) == 2:
        #     return [nums[0], nums[1]] if nums[0] <= nums[1] else [nums[1], nums[0]]

        # mid = len(nums) // 2
        # l, r = [], []

        # for i in range(len(nums)):
        #     if (nums[i] <= nums[mid]) and (i != mid):
        #         l.append(nums[i])
        #     elif nums[i] > nums[mid]:
        #         r.append(nums[i])

        # print(l, r)
        # return self.sortArray(l) + [nums[mid]] + self.sortArray(r)

        # def quickSort(arr, start, end):
        #     if start >= end:
        #         return
        #     index = random.randint(start, end)
        #     pivot = arr[index]
        #     arr[start],arr[index] = arr[index],arr[start]
        #     i, j = start, end
        #     while i<j:
        #         while i<j and arr[j]>=pivot:
        #             j -= 1
        #         while i<j and arr[i]<=pivot:
        #             i += 1
        #         if i != j:
        #             arr[i],arr[j] = arr[j],arr[i]
        #     arr[start], arr[i] = arr[i], arr[start]
        #     quickSort(arr, start, i-1)
        #     quickSort(arr, i+1, end)
        # quickSort(nums, 0, len(nums)-1)
        # return nums


        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/sort-an-array/solution/pai-xu-shu-zu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。