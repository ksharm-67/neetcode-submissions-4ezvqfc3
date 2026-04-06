class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(x):
            return x == x[::-1]
        
        def backtrack(i, curr):
            if i >= len(s):
                res.append(curr[:])
                return

            for j in range(i, len(s)):
                w = s[i : j + 1]
                if isPalindrome(w):
                    curr.append(w)
                    backtrack(j + 1, curr)
                    curr.pop()
               
        res = []
        backtrack(0, [])
        return res  