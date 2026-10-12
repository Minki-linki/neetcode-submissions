class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        f = []
        for i in range(len(s)):
            if s[i] not in d:
                f.append(s[i])
            else:
                if not f or f.pop() != d[s[i]]:
                    return False
        return not f