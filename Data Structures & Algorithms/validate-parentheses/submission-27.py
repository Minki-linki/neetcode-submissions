class Solution:
    def isValid(self, s: str) -> bool:
        group = []
        dict_group = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for char in s:
            if char in dict_group:
                if not group or group[-1] != dict_group[char]:
                     return False
                group.pop()
            else:
                group.append(char)
        return len(group) == 0

