// this code is for counting occrances 

// changes 2
// there are two approch sipmle one and mapmethod
#include<iostream>
using namespace std;
int unique_ele(int arr[],int n){
    int ans=0;
for(int i=0;i<n;i++){
ans=ans^arr[i];
}
return ans;
}
int main(){
    int arr[5]={2,2,3,4,4};
int k=unique_ele(arr,5);
cout<<k;
    return 0;
}