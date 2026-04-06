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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode* temp = head;

        int len = 0;
        while(temp){
            len++;            
            temp = temp->next;
        }

        temp = head;
        int nodeToDel = len - n;
        
        while(--nodeToDel > 0){
            temp = temp->next;
        }

        if (n == len){
            ListNode* newHead = head->next;
            delete head;
            return newHead;
        }

        ListNode* toDel = temp->next;
        temp->next = toDel->next;
        delete toDel;

        return head;
    }
};
