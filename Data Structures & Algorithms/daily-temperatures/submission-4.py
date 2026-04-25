class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day_c = [0] * len(temperatures)
        n = len(temperatures)


        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n  and temperatures[i] >= temperatures[j]:
                if day_c[j] == 0:
                    j = n
                    break
                j += day_c[j]
            if j < n:
                day_c[i] = j - i
        return day_c

        

