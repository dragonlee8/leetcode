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
    void pushFullLeft(TreeNode* root, vector<TreeNode*>& stack) {
        while (root) {
            stack.push_back(root);
            root = root->left;
        }
    }
    int kthSmallest(TreeNode* root, int k) {
        vector<TreeNode*> stack;
        pushFullLeft(root, stack);
        while (stack.size() > 0) {
            auto node = stack.back();
            stack.pop_back();
            k -= 1;
            if (k == 0) {
                return node->val;
            }
            if (node->right) {
                pushFullLeft(node->right, stack);
            }
        }
    }
};
