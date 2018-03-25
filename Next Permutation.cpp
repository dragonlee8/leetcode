class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size(); 
        int p = -1;
        int pre = nums[len-1];
        for (int i = len-2; i >=0; --i ) { 
            if (nums[i] < nums[i+1]) {
                p = i;
                break;
            }
        }

        if (p == -1) {
            sort(nums.begin(), nums.end());
            return;
        }
        
        // Find from p+1:len, the smallest number which is larger than nums[i]
        int min = INT_MAX;
        int p1 = -1; 
        for (int i = p+1 ; i < len; ++i) {
            if (nums[i] > nums[p] && nums[i] < min) {
                min = nums[i];
                p1 = i;
            }
        }
        swap(nums[p], nums[p1]);
        sort(nums.begin() + p +1, nums.end());
        return;
        
    }
};
