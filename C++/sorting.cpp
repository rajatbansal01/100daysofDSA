class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n=nums.size();
        int i=0;int j=n-1;int k=0;
       while(k<=j){
            if(nums[k]==0){
                swap(nums[k],nums[i]);
               i++;k++;
            }         
            else if(nums[k]==1){
                k++;
            }
            else{
                swap(nums[k],nums[j]);
                j--;
            }
        }
    }
};

//this is full code
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int i = 0, j = n - 1, k = 0;
        while (k <= j) {
            if (nums[k] == 0) {
                swap(nums[k], nums[i]);
                i++;
                k++;
            }         
            else if (nums[k] == 1) {
                k++;
            }
            else { // nums[k] == 2
                swap(nums[k], nums[j]);
                j--;
            }
        }
    }
};

int main() {
    vector<int> nums = {2, 0, 2, 1, 1, 0};  // sample input
    Solution sol;
    sol.sortColors(nums);

    cout << "Sorted colors: ";
    for (int x : nums) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}
