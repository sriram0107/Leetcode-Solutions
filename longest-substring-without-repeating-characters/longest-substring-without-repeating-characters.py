class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxthusfar = 0
        best = ""
        for i in range(len(s)):
            if s[i] in best:
                best = best[best.find(s[i]) + 1:] + s[i]
            else:
                best += s[i]
            maxthusfar = max(maxthusfar, len(best))
        return maxthusfar
        