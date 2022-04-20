/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <iostream>
using namespace std;
class BSTIterator {
public:
    vector<int> ans;
    size_t index = 0;
    BSTIterator(TreeNode* root) {
        Traverse(root);
        // for (auto const &i: ans) {
        //     std::cout << i << " ";
        // }
    }
    
    void Traverse(TreeNode* root){
        if(root == nullptr){
            return;
        }
        Traverse(root->left);
        ans.push_back(root->val);
        Traverse(root->right);
        return;
    }
    
    int next() {
        int a = ans[index];
        index++;
        return a;
    }
    
    bool hasNext() {
        if(ans.size() == index){
            return false;
        }
        return true;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */