class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.size() > s2.size()) return false;

        unordered_map<char, int> s1map;
        unordered_map<char, int> s2map;
        for(int i = 0; i < s1.size(); i++){
            s1map[s1[i]]++;
            s2map[s2[i]]++;
        }

        int a = 0;
        for(int j = s1.size(); j < s2.size(); j++){
            if(s1map == s2map) return true;

            s2map[s2[a]]--;
            if(s2map[s2[a]] == 0) s2map.erase(s2[a]);

            s2map[s2[j]]++;
            a++;
        }

        return s1map == s2map;
    }
};
