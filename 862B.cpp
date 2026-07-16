#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
#define ll long long
using namespace std;

int n,m,a,b;
vector<vector<int>> adj;
vector<int> color;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<int>());

    int node = 0;
    m = n-1; while(m--) {
        cin >> a >> b;
        if (!node) node = a;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    
    color.assign(n+1, -1);
    
    vector<int> q1,q2;
    queue<int> q; q.push(node);

    while (!q.empty()) {
        auto x = q.front(); q.pop();

        if (color[x] == -1) color[x] = 1;
        
        if (color[x] == 0) q1.push_back(x);
        else q2.push_back(x);

        for (auto y : adj[x]) {
            if (color[y] != -1) continue;
            
            color[y] = 1-color[x];
            q.push(y);
        }
    }
    
    ll cnt = (ll)q1.size() * q2.size() - (n-1);
    
    cout << cnt << '\n';
}