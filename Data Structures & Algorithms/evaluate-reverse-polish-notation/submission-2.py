class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tok = []
        operation = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        for i in tokens:
            if i in operation:
                a = tok.pop()
                b = tok.pop()
                result = operation[i](b, a)
                tok.append(result)
            else:
                tok.append(int(i))
        return tok.pop()