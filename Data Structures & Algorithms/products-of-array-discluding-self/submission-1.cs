public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] prod = new int[nums.Length];
        int curr = 1;

        for(int i = 0; i < nums.Length; i++) {
            prod[i] = curr;
            curr *= nums[i];
        }

        int prev = 1;
        for(int i = nums.Length - 1; i >= 0; i--) {
            prod[i] *= prev;
            prev *= nums[i];
        }

        return prod;
    }
}
