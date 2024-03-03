class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def something(k: int, piles: List[int], h: int) -> bool:
            total_time=0
            for pile in piles:
                total_time+= (pile-1)//k +1
            return total_time <= h

        n = len(piles)
        left, right = 1, max(piles)
        piles = sorted(piles)

        while left < right:
            mid = (left+right)//2

            if(something(mid,piles,h)):
                right = mid
            else:
                left = mid + 1

        return left