class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s.reverse()

        # failed
        if (len(s)%2==1):
            mid = int((len(s)+1)/2)
            s = s[-1:mid] + s[mid] + s[mid-1:0]
        else:
            l = int(len(s)/2)
            r = l + 1
            s = s[-1:r] + s[r] + s[l] + s[l-1:0]



        