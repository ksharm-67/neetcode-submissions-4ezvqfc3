class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1:
            return stones[0]
        
        stones = [-i for i in stones]
        heapq.heapify(stones)
        heap = stones
        print(len(heap))

        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x == y:
                print(f"{x} == {y}")
                continue
            else:
                print(f"Adding stone of {x - y} weight onto heap")
                heapq.heappush(heap, x - y)
                print(f"new heap: {heap}")

        if not heap:
            return 0
        
        else:
            return -heap[0]
            
        
        