#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
 
int n,m,a,b,s,t;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> n >> m;
    vector<pair<int, int>> edges;
    vector<int> dist(n+1, 1e9);

    while (m--) {
        cin >> a >> b;
        edges.push_back({a,b});
    }

    cin >> s >> t;

    dist[s] = 0;
    for (int i = 1; i < n; i++) {
        for (auto [x,y] : edges) {
            if (dist[x] == 1e9) continue;

            if (dist[x]+1 < dist[y]) dist[y] = dist[x]+1;
        }
    }

    if (dist[t] == 1e9) cout << -1;
    else cout << dist[t];
}