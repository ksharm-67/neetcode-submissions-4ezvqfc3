class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        s1map = {}
        for i in range(len(s1)):
            s1map[s1[i]] = s1map.get(s1[i], 0) + 1
        
        s2map = {}
        for j in range(len(s1)):
            s2map[s2[j]] = s2map.get(s2[j], 0) + 1

        a = 0
        for i in range(len(s1), len(s2)):
            if s1map == s2map:
                return True

            s2map[s2[a]] = s2map.get(s2[a], 0) - 1
            if s2map[s2[a]] == 0:
                del s2map[s2[a]]

            s2map[s2[i]] = s2map.get(s2[i], 0) + 1
            a += 1

        return s1map == s2map
        