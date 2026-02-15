#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int t,n,m,k;
    string cmds;

    cin >> t;
    while (t--) {
        cin >> n >> m >> k;

        vector<int> a(n), b(m);
        map<int, vector<int>> dist;
        vector<bool> removed(n, false);

        for (int i = 0; i < n; i++) cin >> a[i];
        for (int i = 0; i < m; i++) cin >> b[i];

        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        int pos = 0;
        for (int i = 0; i < n; i++) {
            auto it = lower_bound(b.begin(), b.end(), a[i]);
            
            if (it != b.end()) dist[*it - a[i]].push_back(i);
            if (it != b.begin()) dist[*prev(it) - a[i]].push_back(i);
        }

        cin >> cmds;
        pos = 0;

        for (int i = 0; i < k; i++) {
            if (cmds[i] == 'L') pos--;
            else pos++;

            if (dist.count(pos)) {
                for(int idx : dist[pos]) {
                    if (!removed[idx]) {
                        n--;
                        removed[idx] = true;
                    }
                }
                dist.erase(pos);
            }
            cout << n << ' ';
        }
        cout << '\n';
    }
}