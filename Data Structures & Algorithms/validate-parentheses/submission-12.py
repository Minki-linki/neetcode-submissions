class Solution:
    def isValid(self, s: str) -> bool:
        dict_f = {')': '(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i in dict_f:
                if stack and stack[-1] == dict_f[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False