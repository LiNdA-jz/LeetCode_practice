# zip!!!!!!!!
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # not work for
        # "qwertyuiop[]asdfghjkl;'\\zxcvbnm,./"
        # "',.pyfgcrl/=aoeuidhtns-\\;qjkxbmwvz"
        # if len(s) == 1:
        #     return True

        # for i in range(len(s)):
        #     if s.count(s[i]) != t.count(t[i]):
        #         return False

        # for i in range(len(s)):
        #     if re.search(s[i], s).span() != re.search(t[i], t).span():
        #         return False

        # return True

        print(set(zip(s, t)))

        return len(set(s)) == len(set(t)) and len(set(s)) == len(set(zip(s, t)))