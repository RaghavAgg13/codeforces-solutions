#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        for (auto &x : a) cin >> x;

        ll ops = 0;
        int j = 0;
        while (!a[j]) j++;
        for (int i = j; i < n-1; i++) ops += max(1, a[i]);

        cout << ops << endl;
    }
}