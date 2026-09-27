public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length) return false;
        
        Dictionary<char, int> smp = [], tmp = [];
        for(int i = 0; i < s.Length; i++) {
            smp[s[i]] = smp.GetValueOrDefault(s[i]) + 1;
            tmp[t[i]] = tmp.GetValueOrDefault(t[i]) + 1;
        }

        foreach(KeyValuePair<char, int> v in tmp) {
            //Console.WriteLine($"{v.Key}: {v.Value}");        
            if(!tmp.ContainsKey(v.Key) || v.Value != tmp[v.Key]) return false;
        }
        foreach(KeyValuePair<char, int> k in smp) {
            //Console.WriteLine($"{k.Key}: {k.Value}");
            if(!tmp.ContainsKey(k.Key) || k.Value != tmp[k.Key]) {
                return false;
            }
        }
        return true;
    }
}
