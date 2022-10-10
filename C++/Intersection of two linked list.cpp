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
    
    int countNode(ListNode *head){
        ListNode* temp = head;
        int cnt=0;
        while(temp != NULL){
            cnt++;
            temp = temp->next;
        }
        return cnt;
    }
    
   
    
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int count1 = countNode(headA);
        int count2 = countNode(headB);
        
        ListNode* temp1 = headA;
        ListNode* temp2 = headB;
        
        int dif;
        if(count1 > count2){
           dif = count1 - count2; 
        }
        else
            dif = count2 - count1;
        
       if(count1 > count2){
          while(dif != 0){
              temp1 = temp1->next;
              dif--;
          }
           
       }
        if(count2 > count1){
            
            while(dif != 0){
                temp2 = temp2->next;
                dif--;
            }
        }
           
        while(temp1 != NULL && temp2 != NULL){
            if(temp1 == temp2){
                return temp1;
                break; 
            }
               temp1 = temp1->next;
               temp2 = temp2->next;
            
}
        return NULL;
        
    
        
        
    }
};
