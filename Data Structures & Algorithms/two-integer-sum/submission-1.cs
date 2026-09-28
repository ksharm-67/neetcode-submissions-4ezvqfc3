public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // element: index
        Dictionary<int, int> mp = [];
        int complement = 0;

        for(int i = 0; i < nums.Length; i++) {
            complement = target - nums[i];
            if(mp.ContainsKey(complement)) return [mp[complement], i];
            mp[nums[i]] = i;
        }
        return [-1, -1];
    }
}
