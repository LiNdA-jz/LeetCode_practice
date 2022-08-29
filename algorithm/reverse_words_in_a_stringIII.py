class Solution:
    def reverseWords(self, s: str) -> str:
        s_array = s.split()
        for i in range(len(s_array)):
            i_array = list(s_array[i])
            i_array[:] = i_array[::-1]
            s_array[i] = "".join(i_array)
        return " ".join(s_array)


        split_list = s.split(" ")
        split_list = [i[::-1] for i in split_list]
        return " ".join(split_list)

        # first reverse the order of the words and then reverse the entire string.
        return ' '.join(s.split()[::-1])[::-1]

# Time Complexity: O(N)
# Space Complexity: O(1)
# class Solution {
# public:
#     string reverseWords(string s) {
#         string result;
#         int lastSpaceIndex = -1;
#         for (int strIndex = 0; strIndex < s.length(); strIndex++) {
#             if ((strIndex == s.length() - 1) || s[strIndex] == ' ') {
#                 int reverseStrIndex =
#                     (strIndex == s.length() - 1) ? strIndex : strIndex - 1;
#                 for (; reverseStrIndex > lastSpaceIndex; reverseStrIndex--) {
#                     result += s[reverseStrIndex];
#                 }
#                 if (strIndex != s.length() - 1) {
#                     result += ' ';
#                 }
#                 lastSpaceIndex = strIndex;
#             }
#         }
#         return result;
#     }
# };


# Time Complexity: O(N)
# Space Complexity: O(1)
# class Solution {
# public:
#     string reverseWords(string s) {
#         int lastSpaceIndex = -1;
#         int len = (int)s.size();
#         for (int strIndex = 0; strIndex <= len; strIndex++) {
#             if (strIndex == len || s[strIndex] == ' ') {
#                 int startIndex = lastSpaceIndex + 1;
#                 int endIndex = strIndex - 1;
#                 while (startIndex < endIndex) {
#                     char temp = s[startIndex];
#                     s[startIndex] = s[endIndex];
#                     s[endIndex] = temp;
#                     startIndex++;
#                     endIndex--;
#                 }
#                 lastSpaceIndex = strIndex;
#             }
#         }
#         return s;
#     };
# };