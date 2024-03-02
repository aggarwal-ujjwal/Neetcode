class Solution {
public:
    // int count1(int num){
    //     int count = 0;
    //     while(num){
    //         num = num&(num-1);
    //         count++;
    //     }
    //     return count;
    // }

    vector<int> countBits(int n) {
        vector<int> ans(n+1,0);

        // for(int i = 0 ; i <= n ; i++){
        //     ans[i] = count1(i);
        // }
        // return ans;

                       //OR - Most intuitive
//         for(int i = 1 ; i<=n ; i++){
//             ans[i] = ans[i&(i-1)] + 1;
//         }

                    ///OR -  Most important for pattern recognition

        for(int i=0 ; i<=n ; i++){
            ans[i] = ans[i/2] + i%2;
        }

        return ans;
    }
};