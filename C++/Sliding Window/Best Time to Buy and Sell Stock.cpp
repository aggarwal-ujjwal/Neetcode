class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // int n = prices.size(), ans = 0 , max_elem_till_now=prices[n-1];

        // for( int i = n-2 ; i>=0 ; i--){
        //     if(prices[i]<max_elem_till_now)
        //     ans = max(ans, abs(prices[i]-max_elem_till_now));
        //    // min_elem_till_now = min(min_elem_till_now, prices[i]);
        //     max_elem_till_now = max (max_elem_till_now, prices[i]);

        // }
        // return ans;


        int n = prices.size();
        if(n<=1)
            return 0;
        int ans = 0, max_num_till_now= prices[n-1];

        for( int i=n-2 ; i>=0 ; i--){
            if(prices[i] < max_num_till_now)
                ans = max(ans,(max_num_till_now - prices[i]));

            max_num_till_now = max(max_num_till_now,prices[i]);
        }
        return ans;

    }
};