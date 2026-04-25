class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_cnt = ''
        cnt = 0
        cnt_max = 0
        for i in s:
            if i in str_cnt:
                str_cnt = str_cnt[str_cnt.find(i)+1:]
                cnt = len(str_cnt) + 1
                str_cnt += i
            else:
                cnt += 1
                str_cnt += i
            if cnt > cnt_max:
                cnt_max = cnt
        return cnt_max