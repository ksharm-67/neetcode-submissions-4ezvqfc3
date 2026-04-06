class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr, chosen):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if not chosen[i]: 
                    curr.append(nums[i])
                    chosen[i] = True
                    backtrack(curr, chosen)
                    chosen[i] = False
                    curr.pop()

        res, chosen = [], [False for _ in range(len(nums))]
        backtrack([], chosen)
        return res