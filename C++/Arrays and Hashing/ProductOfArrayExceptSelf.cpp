class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefixNum = 1, suffixNum = 1, n = nums.size();
        vector<int> ans(n,1);

        for(int i=0 ; i<n ; i++){
            ans[i] *= prefixNum;
            prefixNum *= nums[i];
            ans[n-i-1] *= suffixNum;
            suffixNum *= nums[n-i-1];
        }

        return ans;
    }
};