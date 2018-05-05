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
};


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
        set<TreeNode*> path;
        vector<TreeNode*> v;
        v.push_back(root);
        while (v.size() > 0) {
            auto node = v.back();
            v.pop_back();
            auto f = path.find(node);
            if (f == path.end()) {
                v.push_back(node);
                if (node->right) {
                    v.push_back(node->right);
                }
                if (node->left) {
                    v.push_back(node->left);
                }
                path.insert(node);
            }
            else {
                ret.push_back(node->val);
            }
        }
        return ret;
    }
};
