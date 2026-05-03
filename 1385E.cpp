    #include <iostream>
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <unordered_map>
    using namespace std;
    #define ll long long

    int q,n,m,t,a,b;

    void solve() {
        cin >> n >> m;
        vector<vector<int>> adj(n+1);
        vector<pair<int, int>> edges;
        vector<int> degree(n+1, 0), top;

        while (m--) {
            cin >> t >> a >> b;
            if (t) {
                adj[a].push_back(b);
                degree[b]++;
            }
            else edges.emplace_back(a,b);
        }

        queue<int> Q;
        for (int i = 1; i <= n; i++) {
            if (!degree[i]) Q.push(i);
        }

        while(!Q.empty()) {
            auto cur = Q.front(); Q.pop();
            top.push_back(cur);

            for (auto x : adj[cur]) {
                if (--degree[x] == 0) Q.push(x);
            }
        }

        if (top.size() != n) {
            cout << "NO\n";
            return;
        }

        unordered_map<int, int> hash;
        for (int i = 0; i < n; i++) hash[top[i]] = i;

        cout << "YES\n";
        for (int x = 1; x <= n; x++) {
            for (auto y : adj[x]) {
                cout << x << ' ' << y << '\n';
            }
        }
        for (auto [x,y] : edges) {
            if (hash[x] > hash[y]) swap(x,y);
            
            cout << x << ' ' << y << '\n';
        }
    }

    int main(void) {
        ios_base::sync_with_stdio(0);
        cin.tie(NULL);

        cin >> q;
        while (q--) solve();
    }