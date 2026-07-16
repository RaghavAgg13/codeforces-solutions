#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
#define ll long long
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;
unordered_map<ll, int> map;
vector<int> idx;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());
    idx.resize(n+1);
    map.clear();
    vector<int> in(n+1, 0);

    for (int i = 1; i < n; i++) {
        cin >> a >> b;

        adj[a].push_back(b);
        adj[b].push_back(a);
        map[1LL*a*n+b] = i; map[a+1LL*b*n] = i;

        in[a]++; in[b]++;
    }

    queue<int> q;
    vector<int> vis(n+1, 0);
    for (int i = 1; i <= n; i++) {
        if (in[i] == 1) {
            q.push(i);
        }
    }
    
    int no = 0;
    while (!q.empty()) {
        auto x = q.front(); q.pop();
        vis[x] = 1;

        for (auto y : adj[x]) {
            if (vis[y]) continue;

            idx[map[1LL*x*n+y]] = no++;
            if (--in[y] == 1) q.push(y);
        }
    }

    for (int i = 1; i < n; i++) {
        cout << idx[i] << '\n';
    }
}