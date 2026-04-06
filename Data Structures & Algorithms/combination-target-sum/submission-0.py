class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def backtrack(nums, index, curr):
            if sum(curr) == target:
                temp = curr[:]
                res.append(temp)
                return 
           
            if index >= len(nums):
                return

            if sum(curr) + nums[index] <= target:
                curr.append(nums[index])
                backtrack(nums, index, curr)
                curr.pop()

            backtrack(nums, index + 1, curr)

        res = []
        backtrack(nums, 0, [])
        return res