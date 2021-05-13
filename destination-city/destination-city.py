class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = self.create(paths)
        for i in graph:
            if graph[i] == []:
                return i
        return ""
    
    def create(self, paths):
        graph = {i[0]:[] for i in paths}
        for i in paths:
            if i[1] not in graph.keys():
                graph[i[1]] = []
            graph[i[0]].append(i[1])
        return graph
            
        