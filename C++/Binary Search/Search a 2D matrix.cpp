class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int left =0 , m = matrix.size() , n= matrix[0].size();
        int right = m*n-1;

        while(left <= right) {
            int mid = left + (right-left)/2;
            // cout << "mid-" << mid << "-left -" << left << "-right-" << right << endl;
            if(matrix[mid/n][mid%n] == target){
                return true;
            }
            else if(matrix[mid/n][mid%n] < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }

        }

        return false;


    }
};

//Note always divide by number of columns to get the matrix indices