class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rowSize = matrix[0].size() - 1;

        int low = 0, high = matrix.size() - 1;

        int targetRow = -1;
        while(low <= high){
            int mid = low + (high - low) / 2;

            if(matrix[mid][rowSize] == target) return true;

            else if(matrix[mid][0] <= target && matrix[mid][rowSize] >= target){
                targetRow = mid;
                break;
            }

            else if(matrix[mid][rowSize] > target) high = mid - 1;

            else low = mid + 1;
        }

        if(targetRow == -1) return false;

        low = 0, high = rowSize;
        while(low <= high){
            int mid = low + (high - low) / 2;

            if(matrix[targetRow][mid] == target) return true;

            else if(matrix[targetRow][mid] < target) low = mid + 1;

            else high = mid - 1; 
        }

        return false;
    }
};
