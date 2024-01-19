class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums) # initialize list with a value
        prefix = 1
        suffix = 1
        n = len(nums)

        for i in range(n):
            ans[i] *= prefix;
            prefix *= nums[i];
            ans[n-i-1] *= suffix;
            suffix *= nums[n-i-1];

        return ans


#make sure you don't use space for storing prefix and suffix