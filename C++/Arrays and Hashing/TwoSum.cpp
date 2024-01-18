class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        int n = nums.size();
        unordered_map<int,int> u_map;
        for(int i=0 ; i<n ; i++){
            u_map[nums[i]]=i+1;
        }

        for(int i=0 ; i<n ; i++){
            if(u_map[target - nums[i]] > 0 && (u_map[target - nums[i]]-1)!= i){
                ans.push_back(i);
                ans.push_back(u_map[target - nums[i]] - 1);
                break;
            }
        }

        return ans;
    }
};