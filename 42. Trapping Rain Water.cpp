class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0) {
            return 0;
        }
        int n = height.size();
        vector<int> left(n, 0);
        int maxl = 0;
        for (int i = 0; i < n; ++i) {
            left[i] = maxl;
            maxl = max(height[i], maxl);
        }
        int accu = 0;
        int maxr = 0;
        for (int i = n-1; i >= 0; --i) {
            int wall = min(maxr, left[i]);
            if (wall > height[i]) {
                accu += wall - height[i];
            }
            maxr = max(maxr, height[i]);
        }
        return accu;
    }
};
