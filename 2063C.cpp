#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int t,n,m,a,b;
vector<vector<int>> adj;
vector<int> deg,is_adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        adj.assign(n+1, vector<int>());
        deg.assign(n+1, 0);
        is_adj.assign(n+1, 0);

        m = n; while (--m) {
            cin >> a >> b;
            adj[a].push_back(b);
            adj[b].push_back(a);
            deg[a]++; deg[b]++;
        }
        
        int max1 = 0, max2 = 0;
        for (int i = 1; i <= n; i++) {
            if (deg[i] > deg[max1]) max1 = i;
        }
        int best_max1 = max1, min_c = n+1;
        for (int i = 1; i <= n; i++) {
            if (deg[i] != deg[max1]) continue;

            int c = 0;
            for (int j : adj[i]) {
                if (deg[j] == deg[max1]) c++;
            }
            if (c < min_c) {
                min_c = c;
                best_max1 = i;
            }
        }
        max1 = best_max1;
        
        for (auto y : adj[max1]) {
            deg[y]--;
            is_adj[y] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            if (i == max1) continue;
            if (max2 == 0 || deg[i] > deg[max2]) max2 = i;
        }
        
        b = deg[max1] + deg[max2]-1;

        cout << b << '\n';
    }
}