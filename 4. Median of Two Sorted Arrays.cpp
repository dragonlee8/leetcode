class Solution {
public:
    double helper(vector<int>& nums1, vector<int>& nums2, int start1, int start2, int k) {
        if (start1 >= nums1.size()) {
            return nums2[start2 + k -1];
        }
                
        if (start2 >= nums2.size()) {
            return nums1[start1 + k -1];
        }
        
        if (k==1) {
            cout <<  min(nums1[start1], nums2[start2]) << endl;
            return min(nums1[start1], nums2[start2]);
        }
        if (nums1.size() < k/2) {
            return helper(nums1, nums2, start1, start2 + k/2, k - k/2);
        }
        
        if (nums2.size() < k/2) {
            return helper(nums1, nums2, start1 + k/2, start2, k - k/2);
        }
        
        if (nums1[start1 + k/2-1] < nums2[start2 + k/2-1]) {
            return helper(nums1, nums2, start1 + k/2, start2, k - k/2);
        }
        else {
            return helper(nums1, nums2, start1, start2 + k/2, k - k/2);
        }
    }
    
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if ((nums1.size() + nums2.size()) %2) {
            return helper(nums1, nums2, 0, 0, (nums1.size() + nums2.size())/2+1);
        }
        
        double a = helper(nums1, nums2, 0, 0, (nums1.size() + nums2.size())/2);
        double b = helper(nums1, nums2, 0, 0, (nums1.size() + nums2.size())/2+1);
        return (a+b)/2;
        
        
    }
};
