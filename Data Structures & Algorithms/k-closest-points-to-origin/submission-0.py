class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distFromOrigin = []
        
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]

            distFromOrigin.append([points[i], x ** 2 + y ** 2])
        
        x = [p[0] for p in heapq.nsmallest(k, distFromOrigin, key = lambda x: x[1])]
        return x