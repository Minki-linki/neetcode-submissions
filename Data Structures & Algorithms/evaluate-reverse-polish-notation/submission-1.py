import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operat = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        summa =[]
        for i in tokens:
            if i in operat:
                a = summa.pop()
                b = summa.pop()
                summa.append(int(operat[i](b,a)))
            else:
                summa.append(int(i))
        return summa[0]
