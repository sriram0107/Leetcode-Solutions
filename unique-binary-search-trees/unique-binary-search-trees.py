class Solution:
    def numTrees(self, n: int) -> int:
        return self.unique(1, n, {})
    
    def unique(self, start, end, hsh):
        if end == 0:
            return 0
        if end - start + 1 in hsh:
            return hsh[end - start + 1]
        unique = 0
        for i in range(start, end + 1):
            left = self.unique(start, i - 1, hsh)
            hsh[i - start] = left
            if left == 0:
                left = 1
            right = self.unique(i + 1, end, hsh)
            hsh[end - i] = right
            if right == 0:
                right = 1
            unique += left * right
        return unique
        