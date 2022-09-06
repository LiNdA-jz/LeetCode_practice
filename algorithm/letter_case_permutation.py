class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # perms = [[]]   
        # for n in s:
        #     new_perms = ""
        #     for perm in perms:
        #         for i in range(len(perm)+1):   
        #             "".join(new_perms, (perm[:i] + [n] + perm[i:]))
        #     perms.append(new_perms)
        # return perms

        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res



        ans = [""]
        for c in S: 
            ans = [x + cc for x in ans for cc in {c, c.swapcase()}]
        return ans 


        """
        :type S: str
        :rtype: List[str]
        """
        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub + S[i], i + 1)
                
        res = []
        backtrack()
        return res