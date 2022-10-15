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
    ListNode* mergeList(ListNode* list1, ListNode* list2){
        ListNode* curnt1 = list1;
        ListNode* next1 = curnt1->next;
        ListNode* curnt2 = list2;
        ListNode* next2;
        
        // for one node only
        if(list1->next == NULL){
            list1->next = curnt2;
            return list1;
        }
        
        while(curnt1 != NULL && next1 != NULL && curnt2 != NULL){
            if(curnt1->val <= curnt2->val && curnt2->val <= next1->val){
                curnt1->next = curnt2;
                next2 = curnt2->next;
                curnt2->next = next1;
                curnt1 = curnt2;
                curnt2 = next2;
            }
            else
            {
                curnt1 = next1;
                next1 = next1->next;
                if(next1 == NULL){
                    curnt1->next = curnt2;
                    return list1;
                }
            }
        }
        return list1;
        
    }
    
   
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == NULL){
            return list2;
        }
        if(list2 == NULL){
            return list1;
        }
        if(list1->val <= list2->val){
            return mergeList(list1,list2);
        }
        else
            return mergeList(list2, list1);
        
        
    }
};
