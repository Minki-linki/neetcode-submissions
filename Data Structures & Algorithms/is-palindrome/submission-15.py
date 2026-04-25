class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = [' ',',','.','!','?',"'",':',';']
        for i in z:
            s = s.lower().replace(i,'')
        if s == s[::-1]:
            return True
        else:
            return False
