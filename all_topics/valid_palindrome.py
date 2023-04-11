class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = []

        for i in range(len(s)):
            if s[i].isalnum():
                rev.append(s[i].lower())

        return rev == rev[::-1]