class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = candidates[:]
        nums.sort()

        def backtrack(i, curr):
            total = sum(curr)
            if total == target:
                res.append(curr[:])
                return

            if total > target or i >= len(nums):
                return

            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr)

        res = []
        backtrack(0, [])

        return res