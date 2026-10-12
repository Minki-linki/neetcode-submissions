class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        steck = [0] * len(temperatures)
        stack = []
        i = 0
        while i != len(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                old = stack.pop()  
                steck[old] = i - old 
            stack.append(i)
            i += 1
        return steck
