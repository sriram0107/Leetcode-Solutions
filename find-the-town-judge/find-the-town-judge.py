class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        graph = self.create(N,trust)
        for i in graph:
            if graph[i]==[] and self.check(i,graph)==N-1:
                return i
        return -1
    
    def create(self, n, trust):
        graph = {i:[] for i in range(1,n+1)}
        for i in trust:
            graph[i[0]].append(i[1])
        return graph
    
    def check(self,i,g):
        score = 0
        for j in g.values():
            if i in j:
                score+=1
        return score

        
    
                