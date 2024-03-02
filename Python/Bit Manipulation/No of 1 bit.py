class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while n:
            n = n&n-1
            ans+=1


        return ans

    #https://leetcode.com/problems/number-of-1-bits/solutions/1044775/python-n-n-1-trick-even-faster-explained/