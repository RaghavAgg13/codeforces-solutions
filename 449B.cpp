#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <climits>
using namespace std;
#define ll long long

int n,m,k,a,b,c;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;
    vector<vector<pair<int, int>>> adj(n+1);
    vector<ll> dist(n+1, LLONG_MAX);
    vector<int> train(n+1, 0);
    int cnt = k;

    while (m--) {
        cin >> a >> b >> c;
        adj[a].emplace_back(b,c);
        adj[b].emplace_back(a,c);
    }

    priority_queue<vector<ll>, vector<vector<ll>>, greater<vector<ll>>> pq;
    pq.push({0, 1, 0});
    dist[1] = 0;

    for (int i = 0; i < k; i++) {
        cin >> a >> b;
        if (dist[a] > b) {
            dist[a] = b;
            train[a] = 1;
        }
    }

    for (int i = 2; i <= n; i++) {
        if (train[i]) pq.push({dist[i], i, 1});
    }

    while (!pq.empty()) {
        auto arr = pq.top(); pq.pop();
        ll d = arr[0], cur = arr[1], isTrain = arr[2];
        
        if (d > dist[cur]) continue;

        for (auto& [x, d_] : adj[cur]) {
        if (d+d_ < dist[x]) {
                dist[x] = d+d_;
                train[x] = 0;
                pq.push({dist[x], x, 0});
            } 
            else if (d+d_ == dist[x]) {
                train[x] = 0;
            }
        }
    }

    int left = 0;
    for (int i = 1; i <= n; i++) left += train[i];
    cout << k-left << '\n';
}