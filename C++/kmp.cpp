#include <bits/stdc++.h>
using namespace std;

vector<int> prefixFunction(string pattern) {
    int m = pattern.size();
    vector<int> lps(m);
    int len = 0;
    for (int i = 1; i < m;) {
        if (pattern[i] == pattern[len]) lps[i++] = ++len;
        else if (len) len = lps[len - 1];
        else lps[i++] = 0;
    }
    return lps;
}

void KMPsearch(string text, string pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> lps = prefixFunction(pattern);

    int i = 0, j = 0;
    while (i < n) {
        if (text[i] == pattern[j]) { i++; j++; }
        if (j == m) {
            cout << "Pattern found at index " << i - j << "\n";
            j = lps[j - 1];
        } else if (i < n && text[i] != pattern[j]) {
            if (j) j = lps[j - 1];
            else i++;
        }
    }
}

int main() {
    string text = "ababcabcabababd";
    string pattern = "ababd";
    KMPsearch(text, pattern);
}
