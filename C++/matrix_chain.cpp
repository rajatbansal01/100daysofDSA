#include <bits/stdc++.h>
using namespace std;

int matrixChainOrder(vector<int>& arr) {
    int n = arr.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int L = 2; L < n; L++) {
        for (int i = 1; i < n - L + 1; i++) {
            int j = i + L - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]);
            }
        }
    }
    return dp[1][n - 1];
}

int main() {
    vector<int> arr = {40, 20, 30, 10, 30};
    cout << "Minimum cost: " << matrixChainOrder(arr) << "\n";
}
