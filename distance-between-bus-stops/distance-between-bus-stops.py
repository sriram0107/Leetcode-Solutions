class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = min(start,destination)
        d = start+destination-s
        s += len(distance)
        fdest = len(distance) + d 
        rdest = d
        distance*=2
        return min(sum(distance[rdest:s]),sum(distance[s:fdest]))
                            
     