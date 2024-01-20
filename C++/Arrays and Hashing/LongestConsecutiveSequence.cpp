class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s; //Here I used set, which gave a TLE, make sure you use unordered one
        for(auto num:nums){
            s.insert(num);
            //cout << num << " ";
        }

        int ans = 0 , seq =0 ;

        for(auto num : nums){
            if(s.find(num-1)==s.end()){ //element not in previous sequences
                seq = num +1;
                //cout << num << " ";
                while(s.find(seq)!=s.end()){
                    seq++;
                }
                ans = max(ans, seq-num);
            }
        }
        return ans;
    }
};