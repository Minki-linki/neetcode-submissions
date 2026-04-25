class Solution:
    def isValid(self, s: str) -> bool:
        stack_del =[]
        mapping = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in mapping:
                if not stack_del or stack_del[-1] != mapping[i]:
                    return False
                stack_del.pop()
            else:
                stack_del.append(i)
        
        return len(stack_del) == 0
