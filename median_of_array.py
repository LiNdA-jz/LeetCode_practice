from ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        len_total = m + n
        if (m>=n):
            for num in nums2:
                total_ls = binSort(nums1, num)
        else:
            for num in nums1:
                total_ls = binSort(nums2, num)

        if ((m+n)%2==0):
            mid = (m+n) / 2
            median = float((total_ls[mid-1]+total_ls[mid]) / 2)

        else:
            mid = (m+n-1) / 2
            median = float(total_ls[mid])
        
        return median
    

def binSort(arr, num):
    arr_len = len(arr)
    if (arr_len%2==0):
        half = int(arr_len / 2)
    else:
        half = int((arr_len+1) / 2)
    new_arr = arr.copy()
    if (num>=arr[-1]):
        new_arr.append(num)
    else:
        left_ls = arr[:half]
        right_ls = arr[half:]
        if (num<left_ls[-1]):
            binSort(left_ls, num)
        else:
            binSort(right_ls, num)
    
    return new_arr
