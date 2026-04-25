class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        d = []
        for i in range(len(temperatures)):
            a = temperatures[i]
            b = i + 1
            while b < len(temperatures) and  a >= temperatures[b]:
                b += 1
            if b == len(temperatures):
                d.append(0)
            else:
               d.append(b - i)
        return d

