class Solution(object):
    def maxArea(self, height):
        length = len(height)
        if length < 2:
            return 0
        i, j = 0, length - 1
        maxthusfar = 0
        while j > i:
            maxthusfar = max(self.area(height[i], i, height[j], j), maxthusfar)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return maxthusfar
        
    
    def area(self, h1, p1, h2, p2):
        return abs(p1 - p2) * min(h1, h2)
        