class Solution(object):
    def maxArea(self, height):
        length = len(height)
        if length < 2:
            return 0
        i, j = 0, length - 1
        maxthusfar = 0
        while j > i:
            maxthusfar = max((j - i) * min(height[i], height[j]), maxthusfar)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxthusfar
        