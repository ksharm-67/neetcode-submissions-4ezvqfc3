class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s:
            return True

        a = 0
        b = len(s) - 1

        while(a < b):
            if s[a].isalnum() and s[b].isalnum():
                if s[a].lower() != s[b].lower():
                    return False
                a += 1
                b -= 1

            elif not s[a].isalnum():
                a += 1
            else:
                b -= 1

        return True

