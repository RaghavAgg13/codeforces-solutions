#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int t,n,m,h;
    cin >> t;
    while (t--) {
        cin >> n >> m >> h;

        vector<int> a(n), b(n);
        vector<pair<int, int>> ops(m);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            b[i] = a[i];
        }

        vector<int> changes;
        int x,y;
        for (int i = 0; i < m; i++) {
            cin >> x >> y;
            a[x-1] += y;
            changes.push_back(x-1);

            if (a[x-1] > h) {
                for (auto x : changes) {
                    a[x] = b[x];
                    changes.clear();
                }
            }
        }

        for (auto &it : a) cout << it << ' ';
        cout << '\n';

    }
}