#include <bits/stdc++.h>
using namespace std;
#define ll long long

int sum_digits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n%10;
        n /= 10;
    }
    return sum;
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int n,q;
        cin >> n >> q;

        vector<int> a(n+1);
        set<int> active_indices;
        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            if (a[i] >= 10) active_indices.insert(i);
        }

        int op, l, r;
        while (q--) {
            cin >> op;

            if (op == 2) {
                cin >> l;
                cout << a[l] << '\n';
            } else {
                cin >> l >> r;

                auto it = active_indices.lower_bound(l);

                while (it != active_indices.end() && *it <= r) {
                    int idx = *it;
                    a[idx] = sum_digits(a[idx]);

                    if (a[idx] < 10) it = active_indices.erase(it);
                    else it++;
                }
            }
        }
    }
}