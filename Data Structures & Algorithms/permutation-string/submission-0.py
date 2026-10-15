class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        for d in range(len(s1)):
            d1[s1[d]] = d1.get(s1[d], 0) + 1
        
        d2 = {}
        cnt = 0
        left, right = 0, 0
        while right != len(s2):
            d2[s2[right]] = d2.get(s2[right], 0) + 1
            cnt += 1
            if cnt == len(s1):
                if d1 == d2:
                    return True
                cnt -= 1
                d2[s2[left]] -= 1
                if d2[s2[left]] == 0:
                    del d2[s2[left]]
                left += 1
            right += 1
        return False
