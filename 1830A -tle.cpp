#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<pair<int, int>> edges, e;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;

        m = n; while (--m) {
            cin >> a >> b;
            edges.push_back({a,b});
        }

        vector<int> vis(n+1, 0);
        vis[1] = 1;

        int cnt = 0;
        while (edges.size()) {
            cnt++;
            e.clear();

            for (auto [x,y] : edges) {
                if (vis[x]+vis[y] == 1) {
                    vis[x] = 1; vis[y] = 1;
                } 
                else if (vis[x]+vis[y] == 0) e.push_back({x,y});
            }
            edges = e;
        }

        cout << cnt << '\n';
    }
    
}