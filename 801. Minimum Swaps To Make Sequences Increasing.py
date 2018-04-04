#include <climits>
class Solution {
public:
    int minSwap(vector<int>& A, vector<int>& B) {
        vector<int> flags(A.size()+1, 0); // -1: need to rotate, 0: don't need rotate, 1: don't need rotate, invalid if rotate
        for (int i = 1; i < A.size(); ++i) {
            if (A[i] > A[i-1] && B[i] > B[i-1]) {
                if (A[i] > B[i-1] && B[i] > A[i-1]) {
                    flags[i] = 0;
                }
                else {
                    flags[i] = 1;
                }
            } 
            else {
                flags[i] = -1;
            }
        }
        flags[A.size()] = 1;
        
        vector<vector<int>> dp(A.size()+1, {0,0});
        for (int i = A.size() - 1; i >=0; --i ) {
            if (flags[i+1] == 1) {
                dp[i][0] = dp[i+1][0];
                dp[i][1] = dp[i+1][1] + 1;
            }
            else {
                if (flags[i+1] == -1) {
                    dp[i][0] = dp[i+1][1];
                    dp[i][1] = dp[i+1][0] +1;
                }
                else {
                    dp[i][0] = min(dp[i+1][0], dp[i+1][1]);
                    dp[i][1] = min(dp[i+1][0], dp[i+1][1]) +1;
                }
            }
        }
        return min(dp[0][0], dp[0][1]);
    }
};
