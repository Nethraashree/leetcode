class Solution:
    def minWindow(self, s, t):
        if t == "":
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            
            while have == need:
                
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""