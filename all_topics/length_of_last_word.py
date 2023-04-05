class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_ls = s.strip().split(" ")
        return len(s_ls[-1])