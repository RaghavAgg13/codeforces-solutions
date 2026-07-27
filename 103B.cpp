#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b,c;
vector<vector<int>> adj;
vector<int> deg;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> n >> m;
    adj.assign(n+1, vector<int>());
    deg.assign(n+1, 0);
    
    c = m; while (c--) {
        cin >> a >> b;
        
        adj[a].push_back(b);
        adj[b].push_back(a);
        deg[a]++; deg[b]++;
    }
 
    queue<int> q;
    for (int i = 1; i <= n; i++) {
        if (deg[i] == 1) {
            deg[i] = 0;
            q.push(i);
        }
    }

    while (!q.empty()) {
        auto x = q.front(); q.pop();
        
        for (auto y : adj[x]) {
            if (--deg[y] == 1) q.push(y);
        }
    }

    // whats left's gotta be a cycle
    a = 0, b = 0;
    for (int i = 1; i <= n; i++) {
        if (deg[i] == 2) {
            if (a == 0) a = i;
            b++;
        }
    }

    if (a == 0 || b < 3 || n != m) {
        cout << "NO";
        return 0;
    }

    q.push(a);
    while (!q.empty()) {
        auto x = q.front(); q.pop();
        deg[x] = 0;
        b--;

        for (auto y : adj[x]) {
            if (deg[y] == 2) {
                q.push(y);
                break;
            }
        }
    }

    if (!b) cout << "FHTAGN!";
    else cout << "NO";
}