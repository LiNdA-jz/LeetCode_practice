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


        # Time complexity is O(n) and additional space is O(1)
        for i in range(len(s)//2): 
            s[i], s[-i-1] = s[-i-1], s[i]

        
        
        # s[:] = s[::-1] is required NOT s = s[::-1] because you have to edit the list inplace.
        # Under the hood, s[:] = is editing the actual memory bytes s points to, and s = points the variable name s to other bytes in the memory.
        s[:] = s[::-1]