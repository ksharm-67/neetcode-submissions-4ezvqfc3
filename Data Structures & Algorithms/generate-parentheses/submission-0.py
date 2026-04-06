class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk = []

        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(stk))
                return
            
            if opened < n:
                stk.append('(')
                backtrack(opened + 1, closed)
                stk.pop()

            if closed < opened:
                stk.append(')')
                backtrack(opened, closed + 1)
                stk.pop()

        res = []
        backtrack(0, 0)
        return res
