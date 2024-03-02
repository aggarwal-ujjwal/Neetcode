class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0] * (n+1)
        for i in range(0,n+1):
            ans[i] = ans[int(i/2)] + i%2

        return ans