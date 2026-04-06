class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []

        for i in range(len(tokens)):

            if tokens[i] not in ['+', '-', '*', '/']:
                stk.append(tokens[i])
            
            else:
                b = int(stk.pop())
                a = int(stk.pop())
                op = tokens[i]
                print(a, op, b)

                if tokens[i] == '+':
                    stk.append(str(a + b))

                elif tokens[i] == '-':
                    stk.append(str(a - b))

                elif tokens[i] == '*':
                    stk.append(str(a * b))

                else:
                    stk.append(str(int(a / b)))

        return int(stk[-1]) 

