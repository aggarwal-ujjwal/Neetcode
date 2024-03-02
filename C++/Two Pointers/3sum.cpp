class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int n = size(nums);
        unordered_map<int,int> umap;
        sort(nums.begin(),nums.end());
        if(n<3 || nums[0]>0)
            return ans;

        for(int i = 0 ; i < n ; i++) {
            umap[nums[i]]=i;
        }

        for (int i = 0 ; i<n-2 ; i++){
            for (int j = i+1 ; j < n-1 ; j++ ){
                int sum = -1*(nums[i]+nums[j]);

                if(umap.count(sum) && umap.find(sum)->second > j) {
                    ans.push_back({nums[i],nums[j],sum});
                }

                j = umap.find(nums[j])->second;

            }
             i = umap.find(nums[i])->second;
        }
        return ans;


//         for(int i=0 ; i<n ; i++){
//             for(int j=i+1 ; j<n-1 ; j++){
//                 vector<int> temp;
//                 int sum = nums[i] + nums[j];
//                 auto it = umap.find(-sum);

//                 if(it != umap.end() && it->second!=i && it->second!=j) {

//                     temp.push_back(nums[i]);
//                     temp.push_back(nums[j]);
//                     temp.push_back(-sum);
//                     sort(temp.begin(),temp.end());
//                     ans.push_back(temp);
//                 }
//             }
//         }

//         sort(ans.begin(),ans.end());
//         ans.erase(unique(ans.begin(),ans.end()),ans.end());


    }
};