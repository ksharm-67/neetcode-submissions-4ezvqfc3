class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        vector<int> res;
        for(int t : temperatures) res.push_back(0);

        stack<int> stk;
        for(int i = temperatures.size() - 1; i >= 0; i--){

            while(!stk.empty() && temperatures[stk.top()] <= temperatures[i]){
                stk.pop();
            }

            if(!stk.empty()) res[i] = stk.top() - i;

            stk.push(i);
        }

        return res;
    }
};
