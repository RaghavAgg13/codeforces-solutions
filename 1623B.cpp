#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int t,n,m,a,b;
vector<pair<int, int>> r;
unordered_map<int, int> par;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        r.clear();

        for (int i = 0; i < n; i++) {
            cin >> a >> b;
            r.push_back({a,b});
        }

        par.clear();
        for (int i = 0; i < n; i++) {
            int ans = (int)1e9, idx = -1;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;

                if (!(r[i].first <= r[j].first && r[i].second >= r[j].second)) continue;

                int val = r[j].first-r[i].first + r[i].second-r[j].second;
                if (val < ans) {
                    ans = val;
                    idx = j;
                }
            }
            par[i] = idx;
        }

        for (int i = 0; i < n; i++) {
            int tar = par[i];
            cout << r[i].first << " " << r[i].second << ' ';

            if (tar == -1) {
                cout << r[i].first << '\n';
            }
            else if (r[i].first == r[tar].first) {
                cout << r[tar].second+1 << '\n';
            }
            else {
                cout << r[tar].first-1 << '\n';
            }
        }
    }
}