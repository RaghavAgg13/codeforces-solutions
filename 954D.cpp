#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;
#define ll long long

int n,m,s,t,a,b;

struct cmp {
    bool operator()(const pair<int, int>& a, const pair<int, int>& b) const {
        return a.second > b.second;
    }
};

vector<vector<int>> adj;

void dijkstra(int start, vector<int>& dist) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> pq;
    dist[start] = 0;
    pq.push({start, 0});

    while (!pq.empty()) {
        auto [cur,d] = pq.top(); pq.pop();
        
        if (d > dist[cur]) continue;
        
        for (auto x : adj[cur]) {
            if (dist[x] <= d+1) continue;

            dist[x] = d+1;
            pq.push({x, dist[x]});
        }
    }
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> s >> t;
    adj.resize(n+1);
    vector<vector<bool>> edge(n+1, vector<bool>(n+1, false));

    while (m--) {
        cin >> a >> b;
        adj[a].emplace_back(b);
        adj[b].emplace_back(a);

        edge[a][b] = true; edge[b][a] = true;
    }

    vector<int> distS(n+1, 1e9);
    dijkstra(s, distS);
    vector<int> distT(n+1, 1e9);
    dijkstra(t, distT);

    int baseline = distS[t], cnt = 0;

    for (int i = 1; i <= n; i++) {
        for (int j = i+1; j <= n; j++) {
            if (edge[i][j]) continue;

            if (distS[i]+1+distT[j] >= baseline && distS[j]+1+distT[i] >= baseline) cnt++;
        }
    }

    cout << cnt;
}