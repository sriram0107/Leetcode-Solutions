class Solution:
    def combinationSum(self, candidates, target):
        res, path = [], []
        self.find(0,candidates,res,path,target)
        return res
    
    def find(self,start,lst,res,path,target):
        s = sum(path)
        if s>target:
            return
        elif s==target:
            res.append(list(path))
        for i in range(len(lst)):
            path.append(lst[i])
            self.find(i,lst[i:],res,path,target)
            path.pop()