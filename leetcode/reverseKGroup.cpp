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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *cur = head;
        ListNode *from = head;
        ListNode *to = head;
        vector<int> klist(k);
        int loopFlag = 1;
        // go to k-th next node
        int count = 0;
        from = cur;
        while(cur){
            if(count == k){
                break;  // find k-th node
            }
            klist[count] = cur->val;
            cur = cur->next;
            count ++;
        };
        to = cur;
        if(count != k){   // remain node count is less than k  -> keep it (not change)
            loopFlag = 0;
        }
        while(loopFlag){
            // change node values
            cur = from;
            for(int i=0;i<k;i++){
                cur->val = klist[k-i-1];
                cur = cur->next;
            }
            
            // go to k-th next node
            cur = to;
            count = 0;
            from = cur;
            while(cur){
                if(count == k){
                    break;
                }
                klist[count] = cur->val;
                cur = cur->next;
                count ++;
            }
            to = cur;
            if(count != k){
                loopFlag = 0;
            };
        };
        return head;
    }
};