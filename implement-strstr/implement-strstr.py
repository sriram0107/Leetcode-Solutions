class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        elif haystack == "":
            return -1
        length = len(needle)
        for pos, char in enumerate(haystack):
            if char == needle[0] and haystack[pos : pos + length] == needle:
                return pos
        return -1
        