class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_stack = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if i in dict_stack and len(stack) != 0 and  stack[-1] == dict_stack[i]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0