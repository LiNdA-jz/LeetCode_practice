class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x_ls = str(x)
        # for i in range(len(x_ls)//2):
        #     if (x_ls[i] != x_ls[-i-1]):
        #         return False
        
        # return True
        return str(x) == str(x)[::-1]