class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n = nums.size(),temp=0;

        for(int i=0 ; i<n ; i++){
            temp = temp^nums[i];
        }
        return temp;
    }
};