class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operate = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        tokens_list = []

        for tok in tokens:
            if tok not in operate:
                tokens_list.append(int(tok))
            else:
                b = tokens_list.pop()
                a = tokens_list.pop()
                tokens_list.append(operate[tok](a, b))
        
        return tokens_list[-1]