class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int,int> u_map;
        for(int i = 0 ; i < n ; i++){
           u_map[nums[i]]++;
           if(u_map[nums[i]] >1){class Solution {
                                 public:
                                     bool containsDuplicate(vector<int>& nums) {
                                         int n = nums.size();
                                         unordered_map<int,int> u_map;
                                         for(int i = 0 ; i < n ; i++){
                                            u_map[nums[i]]++;
                                            if(u_map[nums[i]] >1){
                                                return true;
                                            }
                                        }
                                         return false;
                                     }
                                 };
               return true;
           }
       }
        return false;
    }
};


/*
//first naive solution - traverse the array and match each element with all using 2 for loops - O(n^2)
Brute Force : Idea behind code

Make nested loop , generate all possible pair
Put a condition if both of the number generate in a pair are same
In this approach only the unique pair will be formed because outer loop is running from 0 to n - 1, and inner loop will start from one value extra from previous loop value ( which make it to run n*(n+1)/2 ) .
if we are matching each and every pair of vector , then possibly we can compare if any of them have same value then return true. else at end of nested form loop return false.
*/

