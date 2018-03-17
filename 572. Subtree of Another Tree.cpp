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
    bool helper (TreeNode* s, TreeNode* t, bool isRoot) {
        if (!s && !t) {
            return true;
        }
        else if (!s && t) {
            return false;
        }
        else if (s && !t) {
            return false;
        }
        
        bool ret =  ((s->val == t->val ) && helper(s->left, t->left, false) && helper(s->right, t->right, false)) ;
        if (!isRoot) {
            return ret;
        }
        return (ret || helper(s->left, t, isRoot) || helper(s->right, t, isRoot)); 
    }
    
    bool isSubtree(TreeNode* s, TreeNode* t) {
        return helper(s, t, true);
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
    void serialize(TreeNode* s, std::ostringstream& os) {
        if (!s) {
            os << ",#";
            return;
        }
        os << "," << s->val;
        serialize(s->left, os);
        serialize(s->right, os);
    }
    
    bool isSubtree(TreeNode* s, TreeNode* t) {
        std::ostringstream os1, os2;
        serialize(s, os1);
        serialize(t, os2);
        return os1.str().find(os2.str()) != string::npos;
    }
};
