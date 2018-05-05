/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        if (!root) {
            return ret;
        }
        
        if (root->left) {
            auto leftRet = postorderTraversal(root->left);
            ret.insert(ret.end(), leftRet.begin(), leftRet.end());
        }
        if (root->right) {
            auto rightRet = postorderTraversal(root->right);
            ret.insert(ret.end(), rightRet.begin(), rightRet.end());
        }
        ret.push_back(root->val);
        return ret;
    }
};145. Binary Tree Postorder Traversal
