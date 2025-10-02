#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int u, v, w;
};

int main() {
    int n, m, src;
    cin >> n >> m >> src;
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    vector<int> dist(n, 1e9);
    dist[src] = 0;

    for (int i = 1; i < n; i++) {
        for (auto &e : edges) {
            if (dist[e.u] + e.w < dist[e.v])
                dist[e.v] = dist[e.u] + e.w;
        }
    }

    // check negative cycle
    for (auto &e : edges) {
        if (dist[e.u] + e.w < dist[e.v]) {
            cout << "Negative cycle detected\n";
            return 0;
        }
    }

    cout << "Shortest distances from source:\n";
    for (int i = 0; i < n; i++) cout << dist[i] << " ";
    cout << "\n";
}
