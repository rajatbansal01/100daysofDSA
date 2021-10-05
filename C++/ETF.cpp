
//phi gives us the count of all numbers
//that are smaller than the given number
//and are coprime with that number

//phi(prime numbers) = prime number - 1;

#include<bits/stdc++.h>
using namespace std;
//phi(x) = n(1-1/p1)(1-1/p2)(1-1/p3)...
//where p1,p2,p3 are prime factors of x.

int phi(int n) {
    int result = n;
    //since every factor comes in pair so sqrt(n)
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0)
                n /= i;
            //phi(n) = n(1-1/p1)(1-1/p2)...
            //       = (n-n/p1)(1-1/p2)
          
            // let (n-n/p1) = x
          
            //phi(n) = (x-x/p2)...
            //.......
            //.......
            result -= result / i;
        }
    }
    if (n > 1)
        result -= result / n;
    return result;
}

int main(){
  cout<<phi(23)<<"\n";
  //Time complexity O(sqrt(n))
  return 0;
}
