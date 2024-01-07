/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* cur = head;
        if(!head || !(head->next)){
            return head;
        }
        while(cur){
            // find the node with same value with cur (cur .. curEnd)
            ListNode *curEnd = cur->next;
            while(curEnd){
                if(cur->val == curEnd->val){
                    curEnd = curEnd->next;
                } else {
                    break;
                }
            }
            if(cur->next == curEnd){  // this node is not duplicated
                prev = cur;
                cur = cur->next;
            } else {   // duplicated between cur .. curEnd
                if(!prev){    // start node
                    head = curEnd;
                    cur = curEnd;
                } else {
                    prev->next = curEnd;
                    cur = curEnd;
                }
            }
            
        }
        return head;
    }
};