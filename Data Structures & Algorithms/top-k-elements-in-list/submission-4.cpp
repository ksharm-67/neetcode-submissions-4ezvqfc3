class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        vector<vector<int>> bucket(nums.size() + 1);
        
        unordered_map<int, int> freq;
        for(auto n : nums){
            freq[n]++;
        }
        
        cout << endl;

        for(auto f : freq){
            bucket[f.second].push_back(f.first);
        }

        vector<int> res;
        for(int l = bucket.size() - 1; l >= 0 && k > 0; l--){
            for(int x : bucket[l]){
                res.push_back(x);
                k--;
                if(k == 0) break;
            }
        }

        return res;
    }
};
