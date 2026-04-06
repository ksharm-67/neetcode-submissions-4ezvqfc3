class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        time, mp = 0, Counter(tasks)

        maxHeap, q = [-i for i in mp.values()], deque()
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            if maxHeap:
                x = heapq.heappop(maxHeap)
                if (x + 1) < 0:
                    timeAvailable = time + n
                    q.append((x + 1, timeAvailable))
            
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time


