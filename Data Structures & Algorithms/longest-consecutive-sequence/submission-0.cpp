class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        int longest = 0, currLen = 0, nextNum = 0;
        unordered_map<int, bool> mp;

        for(int i : nums) mp[i] = false;

        for(int j = 0; j < nums.size(); j++){
            if(mp.find(nums[j] - 1) == mp.end()){
                currLen = 1;
                mp[nums[j]] = true;

                nextNum = nums[j] + 1;
                while(mp.find(nextNum) != mp.end() && mp[nextNum] == false){
                    currLen++;
                    mp[nextNum] = true;
                    nextNum++;
                }
                
                longest = max(longest, currLen);
            }
        }
        return longest;
    }
};
