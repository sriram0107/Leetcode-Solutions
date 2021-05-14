from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hsh = Counter(nums)
        ans = []
        for i in hsh:
            if hsh[i] > 1:
                ans.append(i)
        return ans
        