class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        vector<char> seen;
        int longest = 0;

        int temp = 0;
        for(int i = 0; i < s.size(); i++){

            auto index = find(seen.begin(), seen.end(), s[i]);
            
            if(index == seen.end()){
                temp++;
                seen.push_back(s[i]);
            }
            else{
                longest = max(longest, temp);

                seen.erase(seen.begin(), index + 1);
                seen.push_back(s[i]);
                temp = seen.size();
            }
        }

        return max(longest, temp);
    }
};
