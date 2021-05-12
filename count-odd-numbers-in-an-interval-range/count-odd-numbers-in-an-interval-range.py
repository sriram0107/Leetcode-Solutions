class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        if low%2==0:
            low = low+1
        return ceil((high-low+1)/2)
            
        