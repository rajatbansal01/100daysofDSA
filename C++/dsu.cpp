#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> parent, rank;
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    void unite(int x, int y) {
        x = find(x), y = find(y);
        if (x != y) {
            if (rank[x] < rank[y]) swap(x, y);
            parent[y] = x;
            if (rank[x] == rank[y]) rank[x]++;
        }
    }
};

int main() {
    DSU dsu(5);
    dsu.unite(0, 1);
    dsu.unite(3, 4);
    cout << (dsu.find(0) == dsu.find(1)) << "\n"; // 1
    cout << (dsu.find(0) == dsu.find(2)) << "\n"; // 0
}
