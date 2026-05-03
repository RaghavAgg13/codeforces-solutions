#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b,c,i,new_cost,new_temp;

struct cmp {
    bool operator()(const vector<int>& a, const vector<int>& b) const {
        return a[1] > b[1];
    }
};

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    vector<vector<pair<int, int>>> adj(n+1);
    vector<vector<int>> dist(n+1, vector<int>(51, 1e9));

    while (m--) {
        cin >> a >> b >> c;
        adj[a].emplace_back(b,c);
        adj[b].emplace_back(a,c);
    }

    priority_queue<vector<int>, vector<vector<int>>, cmp> pq;
    pq.push({1, 0, 0});

    dist[1][0] = 0;
    while (!pq.empty()) {
        auto arr = pq.top(); pq.pop();
        int cur = arr[0], d = arr[1], temp = arr[2];
        
        if (d > dist[cur][temp]) continue;
        
        for (auto [x, d_] : adj[cur]) {
            new_cost = d + (temp == 0 ? 0 : (d_+temp)*(d_+temp));
            new_temp = (temp ? 0 : d_);

            if (new_cost >= dist[x][new_temp]) continue;
            dist[x][new_temp] = new_cost;
            
            pq.push({x, dist[x][new_temp], new_temp});
        }
    }

    for (i = 1; i <= n; i++) cout << (dist[i][0] == 1e9 ? -1 : dist[i][0]) << ' ';
    cout << '\n';

}