class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in arr1:
            count = 0
            for j in arr2:
                if abs(j - i) <= d:
                    count += 1
                    break
            if count == 0:
                ans += 1
        return ans
                
        