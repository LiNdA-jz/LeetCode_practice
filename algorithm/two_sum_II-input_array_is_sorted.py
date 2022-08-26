class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers: O(n) time and O(1) space

        l, r = 0, len(numbers)-1

        while (l<r):
            if (numbers[l]+numbers[r]>target):
                r -= 1
            elif (numbers[l]+numbers[r]<target):
                l += 1
            else:
                return [l+1,r+1]

        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1


        # dict
        # Dictionary: O(n) time and O(n) space

        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

        
        # binary search
        # Binary search: O(nlogn) time and O(1) space
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1