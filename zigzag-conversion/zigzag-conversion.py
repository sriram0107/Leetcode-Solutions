class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        pattern = [[] for i in range(numRows)]
        currRow = 0
        desc = True
        for char in s:
            pattern[currRow].append(char)
            if currRow == numRows - 1:
                desc = False
            elif currRow == 0:
                desc = True
            if desc:
                currRow += 1
            else:
                currRow -= 1
        ans = ""
        for i in pattern:
            ans += "".join(i)
        return ans
        
        
            
            