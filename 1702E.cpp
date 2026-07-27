#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,n,m,a,b;
vector<int> dsu,freq;

int find(int x) {
    if (dsu[x] < 0) return x;
    return dsu[x] = find(dsu[x]);
}

void merge(int x, int y) {
    x = find(x);
    y = find(y);

    if (x == y) return;

    if (dsu[x] <= dsu[y]) {
        dsu[x] += dsu[y];
        dsu[y] = x;
    } else {
        dsu[y] += dsu[x];
        dsu[x] = y;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        dsu.assign(n+1, -1);
        freq.assign(n+1, 0);

        m = n; while (m--) {
            cin >> a >> b;
            merge(a,b);
            freq[a]++; freq[b]++;
        }

        bool pos = true;
        for (int i = 1; i <= n; i++) {
            if ((dsu[i] < 0 && (-dsu[i])%2) || (freq[i] != 2)) {
                cout << "NO\n";
                pos = false;
                break;
            }
        }

        if (pos) cout << "YES\n";
    }
}