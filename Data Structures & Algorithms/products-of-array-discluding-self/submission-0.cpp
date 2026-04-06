class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        vector<int> prod;

        int p = 1;
        for(int i = 0; i < nums.size(); i++){
            if(i == 0) prod.push_back(1);
            else{
                p *= nums[i - 1];
                prod.push_back(p);
            }
        }
        for(auto pr : prod) cout << pr << " ";

        p = 1;
        for(int j = nums.size() - 1; j >= 0; j--){
            prod[j] *= p;
            p *= nums[j];
        }
        for(auto pro : prod) cout << pro << " ";

        return prod;
    }
};
