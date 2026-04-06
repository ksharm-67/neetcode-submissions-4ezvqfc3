class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, index, curr):

            if index >= len(nums):
                temp = curr[:]
                res.append(temp)
                return

            curr.append(nums[index])
            backtrack(nums, index + 1, curr)
            curr.pop()
            backtrack(nums, index + 1, curr)


        res  = []
        backtrack(nums, 0, [])
        return res 