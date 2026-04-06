class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int a = 0;
        int b = numbers.size() - 1;

        while(a < b){
            int ans = numbers[a] + numbers[b];
            if(ans == target) return {a + 1, b + 1};
            else if(ans > target) b--;
            else a++;
        }
        return {};
    }
};
