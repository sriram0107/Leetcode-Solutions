class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0 for i in T]
        for i in range(len(T)):
            if len(stack)!=0 and T[i] > stack[-1][0]:
                while T[i] > stack[-1][0]:
                    x = stack.pop()
                    res[x[1]]=i-x[1]
                    if len(stack)==0:
                        break
            stack.append([T[i],i])
        return res
        
    

    