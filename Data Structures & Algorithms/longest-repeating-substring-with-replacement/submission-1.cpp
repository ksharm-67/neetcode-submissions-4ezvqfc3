class Solution {
public:
    int characterReplacement(string s, int k) {
        
        int window = 0, maxWind = 0, a = 0, maxFreq = 0;

        unordered_map<char, int> mp;
        for(int i = 0; i < s.size(); i++){
            mp[s[i]]++;
            maxFreq = max(maxFreq, mp[s[i]]);

            window = i - a + 1;
            
            if(window - maxFreq > k){
                mp[s[a]]--;
                a++;
            }

            window = i - a + 1;
            maxWind = max(window, maxWind);
        }
        return maxWind;
    }
};
