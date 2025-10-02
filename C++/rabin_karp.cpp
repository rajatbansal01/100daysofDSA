#include <bits/stdc++.h>
using namespace std;

#define d 256
#define q 101 // prime number

void rabinKarp(string txt, string pat) {
    int n = txt.size(), m = pat.size();
    int h = 1, p = 0, t = 0;

    for (int i = 0; i < m - 1; i++) h = (h * d) % q;

    for (int i = 0; i < m; i++) {
        p = (d * p + pat[i]) % q;
        t = (d * t + txt[i]) % q;
    }

    for (int i = 0; i <= n - m; i++) {
        if (p == t) {
            if (txt.substr(i, m) == pat) {
                cout << "Pattern found at index " << i << "\n";
            }
        }
        if (i < n - m) {
            t = (d * (t - txt[i] * h) + txt[i + m]) % q;
            if (t < 0) t += q;
        }
    }
}

int main() {
    string text = "GEEKS FOR GEEKS";
    string pat = "GEEK";
    rabinKarp(text, pat);
}
