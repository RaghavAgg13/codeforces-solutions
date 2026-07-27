#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
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
    vector<map<int, int>> c_map(m_color+1, map<int, int>());
    vector<int> q(m_color+1, 0);

    while (m--) {
        cin >> a >> b;
        if (color[a] == color[b]) continue;

        if (!c_map[color[a]][color[b]]) {
            c_map[color[a]][color[b]] = 1;
            q[color[a]]++;
        }

        if (!c_map[color[b]][color[a]]) {
            c_map[color[b]][color[a]] = 1;
            q[color[b]]++;
        }
    }

    b = color[1];
    for (int i = 2; i <= n; i++) {
        int cur_c = color[i];
        if (q[cur_c] > q[b]) b = cur_c;
        else if (q[cur_c] == q[b] && cur_c < b) b = cur_c;
    }

    cout << b << '\n';
}