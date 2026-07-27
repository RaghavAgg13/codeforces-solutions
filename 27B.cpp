#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;
vector<int> in;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    m = (n*(n-1))/2;
    in.resize(n+1, 0);
    adj.resize(n+1, vector<int>());
    unordered_map<int, int> map;

    while (--m) {
        cin >> a >> b;
        adj[a].push_back(b);
        
        in[b]++;
        map[a*100+b] = 1;
    }
    
    queue<int> q;
    for (int i = 1; i <= n; i++) {
        if (!in[i]) q.push(i);
    }

    vector<int> topo = {-1};
    while (!q.empty()) {
        auto x = q.front(); q.pop();
        topo.push_back(x);

        for (auto y : adj[x]) {
            if (--in[y] == 0) q.push(y);
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = i+1; j <= n; j++) {
            int x = topo[i], y = topo[j];

            if (map[x*100+y]) continue;
            cout << x << ' ' << y;
            return 0;
        }
    }
}