class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
            
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    
#     dfs(nums = [1, 2, 3] , path = [] , result = [] )
# |____ dfs(nums = [2, 3] , path = [1] , result = [] )
# |      |___dfs(nums = [3] , path = [1, 2] , result = [] )
# |      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
# |           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
# |           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
#        |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
#             |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result

    # 
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        ans = []
        backtrack(0, len(nums))
        return ans



    # add the nth number into the resulting List<List<Integer>> from the n-1 numbers
    # For example, if the input num[] is {1,2,3}: First, add 1 into the initial List<List<Integer>>
    # Then, 2 can be added in front or after 1. So we have to copy the List in answer (it's just {1}), 
    # add 2 in position 0 of {1}, then copy the original {1} again, and add 2 in position 1. 
    # Now we have an answer of {{2,1},{1,2}}. There are 2 lists in the current answer.
    # Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0; then copy {2,1} and {1,2}, 
    # and add 3 into position 1, then do the same thing for position 3. Finally we have 2*3=6 lists in answer, which is what we want.
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
        return perms