#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to, weight;
};

int main() {
    int n, m;
    cout << "Enter number of vertices and edges: ";
    cin >> n >> m;

    vector<vector<Edge>> adj(n);

    cout << "Enter edges (u v w):\n";
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w}); // undirected graph
    }

    vector<int> key(n, INT_MAX);   // min edge weight to connect
    vector<int> parent(n, -1);     // MST parent
    vector<bool> inMST(n, false);  // included in MST?

    // Min-heap for selecting edge with minimum weight
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;

    key[0] = 0;
    pq.push({0, 0}); // (weight, vertex)

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if (inMST[u]) continue;
        inMST[u] = true;

        for (auto &edge : adj[u]) {
            int v = edge.to;
            int w = edge.weight;
            if (!inMST[v] && w < key[v]) {
                key[v] = w;
                parent[v] = u;
                pq.push({key[v], v});
            }
        }
    }

    cout << "\nEdges in Minimum Spanning Tree:\n";
    int totalWeight = 0;
    for (int i = 1; i < n; i++) {
        cout << parent[i] << " - " << i << " (weight " << key[i] << ")\n";
        totalWeight += key[i];
    }
    cout << "Total weight of MST = " << totalWeight << "\n";

    return 0;
}
