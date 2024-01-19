class Solution {
    static bool cmp(pair<int,int>& a, pair<int,int>& b){
        return a.second>b.second; //Descending order, first element should be bigger
    }
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> ans;

        unordered_map<int,int> umap;

        for(auto num:nums){
            umap[num]++;
        }

        //Create vector to store elements and frequency
        vector<pair<int,int>> v;
        for(auto x : umap){
            v.push_back(pair{x.first,x.second});
        }

        //sort based on comparator
        sort(v.begin(), v.end(), cmp);

        for (int i = 0 ; i < k ; i++){
            auto it = v.begin() + i;
            ans.push_back(it->first);
            //ans.push_back(v[i]->first) - not acceptable
        }
        return ans;
    }
};


//See how to solve with priority queue