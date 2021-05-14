from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hsh = Counter(arr)
        l = len(arr)
        for i in hsh:
            if (hsh[i]*100)/l > 25:
                return i
        