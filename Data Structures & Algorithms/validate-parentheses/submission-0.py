class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True
        
        brack = []

        for i in range(len(s)):
            if s[i] in '({[':
                brack.append(s[i])
            if s[i] == ')':
                if brack and brack[-1] == '(':
                    brack.pop()
                else:
                    brack.append(s[i])
            elif s[i] == '}':
                if brack and brack[-1] == '{':
                    brack.pop()
                else:
                    brack.append(s[i])
            elif s[i] == ']':
                if brack and brack[-1] == '[':
                    brack.pop()
                else:
                    brack.append(s[i])

        return not brack                        