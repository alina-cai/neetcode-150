class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        countT = {}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        need = len(countT)
        have = 0
        window = {}
        res = float('inf'), None, None
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1

            while need == have:
                if r - l + 1 < res[0]:
                    res = r - l + 1, l, r

                window[s[l]] -= 1
                
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return "" if res[0] == float('inf') else s[res[1]:res[2] + 1]

# time: O(m + n)
# space: O(n)
