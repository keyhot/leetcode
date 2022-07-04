class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        while True:
            n = len(s)
            if n == 0:
                break

            if s[n - 1] == 'I':
                ans += 1
                s = s[:n - 1]
            elif s[n - 1] == 'V' and s[n - 2] == 'I':
                ans += 4
                s = s[:n - 2]
            elif s[n - 1] == 'V':
                ans += 5
                s = s[:n - 1]
            elif s[n - 1] == 'X' and s[n - 2] == 'I':
                ans += 9
                s = s[:n - 2]
            elif s[n - 1] == 'X':
                ans += 10
                s = s[:n - 1]
            elif s[n - 1] == 'L' and s[n - 2] == 'X':
                ans += 40
                s = s[:n - 2]
            elif s[n - 1] == 'L':
                ans += 50
                s = s[:n - 1]
            elif s[n - 1] == 'C' and s[n - 2] == 'X':
                ans += 90
                s = s[:n - 2]
            elif s[n - 1] == 'C':
                ans += 100
                s = s[:n - 1]
            elif s[n - 1] == 'D' and s[n - 2] == 'C':
                ans += 400
                s = s[:n - 2]
            elif s[n - 1] == 'D':
                ans += 500
                s = s[:n - 1]
            elif s[n - 1] == 'M' and s[n - 2] == 'C':
                ans += 900
                s = s[:n - 2]
            elif s[n - 1] == 'M':
                ans += 1000
                s = s[:n - 1]
            else:
                break
        return ans