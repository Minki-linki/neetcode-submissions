class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        steck = []
        d = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        for token in tokens:
            if token not in d:
                steck.append(int(token))
            else:
                b = steck.pop()
                a = steck.pop()
                steck.append(d[token](a, b))
        return steck[0]