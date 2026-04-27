class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operat = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        res = []
        for i in tokens:
            if i in operat:
               b = res.pop()
               a = res.pop()
               a = operat[i](a,b)
               res.append(a)
            else:
                res.append(int(i))
        return res[0]