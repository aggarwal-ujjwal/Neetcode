class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        for i in range(0,n):
            ans^=i
            ans^=nums[i]

        return ans
