class Solution(object):
    def romanToInt(self, s):
        convert = self.convertHash()
        num = 0
        strlen = len(s)
        i = 0
        while i < strlen:
            if i == strlen - 1:
                num += convert[s[i]]
            elif convert[s[i]] < convert[s[i + 1]]:
                num += (convert[s[i + 1]] - convert[s[i]])
                i += 1
            else:
                num += convert[s[i]]
            i += 1
        return num
            
        
    def convertHash(self):
        hsh = {}
        hsh["I"] = 1
        hsh["V"] = 5
        hsh["X"] = 10
        hsh["L"] = 50
        hsh["C"] = 100
        hsh["D"] = 500
        hsh["M"] = 1000
        return hsh