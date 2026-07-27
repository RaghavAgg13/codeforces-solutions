#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
vector<vector<int>> adj;
vector<int> color;

int n,m,a,b;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    color.resize(n+1);
    int m_color = 0;
    
    for (int i = 1; i <= n; i++) {
        cin >> color[i];
        m_color = max(m_color, color[i]);
    }
    
    adj.assign(m_color+1, vector<int>());

    while (m--) {
        cin >> a >> b;
        if (color[a] == color[b]) continue;

        adj[color[a]].push_back(color[b]);
        adj[color[b]].push_back(color[a]);
    }

    b = color[1];
    int cnt = -1;
    for (int i = 1; i <= m_color; i++) {
        if (adj[i].size() == 0) continue;

        sort(adj[i].begin(), adj[i].end());
        int new_cnt = unique(adj[i].begin(), adj[i].end()) - adj[i].begin();

        if (new_cnt > cnt) {
            b = i;
            cnt = new_cnt;
        }
        else if (new_cnt == cnt && i < b) {
            b = i;
        }
    }

    if (cnt == -1) {
        for (int i = 2; i <= n; i++) b = min(b, color[i]);
    }

    cout << b << '\n';
}