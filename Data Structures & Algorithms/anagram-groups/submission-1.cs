public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> mp = [];

        for(int i = 0; i < strs.Length; i++) {
            List<char> word = strs[i].ToList();
            word.Sort();
            string joined = string.Join("", word);
            if(mp.ContainsKey(joined)) mp[joined].Add(strs[i]);
            else mp[joined] = [strs[i]];
        }

        List<List<string>> res = [];
        foreach(var (k, v) in mp) {
            res.Add(v);
        }

        return res;
    }
}
