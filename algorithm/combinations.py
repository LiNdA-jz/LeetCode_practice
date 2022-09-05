class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # num_ls = [i+1 for i in range(n)]

        # res = []
        
        # recursive
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]


        # iterative
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs

        combs = [[]]
        for _ in range(k):
            temp = []
            for c in combs:
                for i in range(1, c[0] if c else n+1):
                    temp.append([i]+c)
            combs = temp
        return combs

        # iterative using reduce
        return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)],
                  range(k), [[]])

# library
from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))



# backpropagation
# backtracking algorithms are often much faster than the brute-force search algorithm
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
# enumeration of candidates is done in two levels:
# 1. the function is implemented as recursion. At each occurrence of recursion, the function is one step further to the final solution.
# 2. within the recursion, we have an iteration that allows us to explore all the candidates that are of the same progress to the final solution
# could solve the problem with the paradigm of backtracking.
    sol=[]
    def backtrack(remain,comb,nex):
        # solution found
        if remain==0:
            sol.append(comb.copy())
        else:
            # iterate through all possible candidates
            for i in range(nex,n+1):
                # add candidate
                comb.append(i)
                #backtrack
                backtrack(remain-1,comb,i+1)
                # remove candidate
                comb.pop()
        
    backtrack(k,[],1)
    return sol