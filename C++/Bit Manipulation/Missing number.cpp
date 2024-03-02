class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();

        // int sum1 = n*(n+1)/2, sum2=0;

        // for(int i = 0 ; i<n ; i++){
        //     sum2 += nums[i];
        // }

        // return sum1-sum2;
        int ans =0;
        for(int i=0 ; i<n ; i++){
            ans^=i;
            ans^=nums[i];
        }
        return ans^n;
    }
};

//Don't forget the last extra XOR with n as that is not done with for loop