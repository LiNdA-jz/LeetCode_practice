import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(needle, haystack)
        if match:
            return match.start()
        else:
            return -1