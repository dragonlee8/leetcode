class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        if (matrix.size() == 0) {
            return 0;
        }
        int height = matrix.size();
        int length = matrix[0].size();
        int maxV = INT_MIN;
        for (int i = 0; i < length; ++i) 
        {
            vector<int> dp(height, 0);
            for (int j = i; j < length; ++j) {
                for (int row = 0; row < height; ++row) {
                    dp[row] += matrix[row][j];
                }
                int cuSum = 0;
                set<int> sum;
                sum.insert(0);
                for (int r = 0; r < height; ++r ) {
                    cuSum += dp[r];
                    auto it = sum.lower_bound(cuSum - k);
                    if (it != sum.end()) {
                        maxV = max(maxV, cuSum - *it);
                    }
                    sum.insert(cuSum);
                }
            }
        }
        return maxV;
    }
};
