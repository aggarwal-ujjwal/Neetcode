class Solution {
public:
    bool something(int k,vector<int>& piles, int h){
        int totalTime=0;
        for (int banana : piles){
            int time_for_pile = (banana - 1) / k + 1; //ceil as 8/4 gives 2 but we are addind one already
            totalTime += time_for_pile;
            }
            return totalTime <= h;
        }

    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(),piles.end());
        int max_p=0 , n = piles.size(), ans=0;
        for(int i = 0 ; i<n ; i++){
            max_p=max(max_p,piles[i]);
        }
        int left = 1 , right = max_p;

        while(left<right){
            int mid = left + (right-left)/2;

            if (something(mid,piles,h)){
                right = mid;}
            else{
                left = mid+1;
            }
        }
        return left;
    }
};