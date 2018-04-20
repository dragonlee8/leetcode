/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode* h = head;
        if (!head) {
            return nullptr;
        }
        int cnt = 0;
        while (h) {
            cnt ++;
            h = h->next;
        }
        
        int rotates = k % cnt;
        
        if (!head->next || rotates == 0) {
            return head;
        }
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* newHead = head;
        for (int i = 0; i < rotates; ++i) {
            fast = fast->next;
        }
        while (fast->next) {
            fast = fast->next;
            slow = slow->next;
        }
        
        newHead = slow->next;
        fast->next = head;
        slow->next = nullptr;
        return newHead;
    }
};
