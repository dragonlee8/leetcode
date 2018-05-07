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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* h = new ListNode(0);
        h->next = head;
        auto pre = h;
        int preVal = 0;
        while (head) {
            while (head->next && head->val == head->next->val) {
                head = head->next;
            }
            if (pre->next == head) {
                pre = head;
            }
            else {
                pre->next = head->next;
            }
            head = head->next;
        }
        
        return h->next;
    }
};
