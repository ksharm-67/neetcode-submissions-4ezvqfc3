class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        mp = {}
        a, windowSize = 0, 0
        maxWindow, maxFreq = 0, 0 

        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0) + 1

            maxFreq = max(maxFreq, mp[s[i]])
            windowSize = i - a + 1

            if(windowSize - maxFreq > k):
                mp[s[a]] -= 1
                a += 1

            windowSize = i - a + 1
            maxWindow = max(maxWindow, windowSize)

        return maxWindow