class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #start with the station that has the most gas
        if sum(gas)<sum(cost):
            return -1
        result = 0
        total = 0

        for i in range(len(gas)):
            # result = i
            
            total += gas[i]-cost[i]
            if total < 0:
                total = 0
                result = i+1
        return result
            


        