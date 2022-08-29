class Solution:
    def reverseWords(self, s: str) -> str:
        s_array = s.split()
        for i in range(len(s_array)):
            i_array = list(s_array[i])
            i_array[:] = i_array[::-1]
            s_array[i] = "".join(i_array)
        return " ".join(s_array)