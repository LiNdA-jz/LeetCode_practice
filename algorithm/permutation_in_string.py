class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # only passed test cases with len(s1)==2
        if (len(s1)>len(s2)):
            temp = s1
            s1 = s2
            s2 = temp
        
        s1_rev = "".join(list(s1)[::-1])
        print(s1_rev)
        l, r = 0, len(s2)-1
        
        while (l < r):
            if (s2[l:r+1]==s1):
                return True
            elif (s2[l]==s1[0]):
                r -= 1
            else:
                l += 1
        l, r = 0, len(s2)-1
        while (l < r):
            if (s2[l:r+1]==s1_rev):
                return True
            elif (s2[l]==s1_rev[0]):
                r -= 1
            else:
                l += 1

        return False