class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        # left sliding window
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                # remove repeating character
                charSet.remove(s[l])
                l += 1
            # add to set
            charSet.add(s[r])
            # current res = r-l+1
            res = max(res, r-l+1)

        return res

        # dict
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

        # We use a dictionary to store the character as the key, the last appear index has been seen so far as value.
        # seen[charactor] = index
        # Time complexity :O(n). n is the length of the input string. It will iterate n times to get the result.

        # Space complexity: O(m). m is the number of unique characters of the input. We need a dictionary to store unique characters.
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            
            There are two cases if s[r] in seen:
            case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            case2: s[r] is not inside the current window, we can keep increase the window
            """
            if s[r] not in seen:
                output = max(output,r-l+1)
            
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output