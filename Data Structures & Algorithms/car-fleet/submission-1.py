class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        st = [(position[i], speed[i]) for i in range(len(position))]
        st.sort(reverse = True)
        #print(st)

        res = 0

        destTime, currTime = 0, 0
        for pos, tm in st:
            destTime = (target - pos) / tm
            #print(destTime)

            if destTime > currTime:
                res += 1
                currTime = destTime

        return res 