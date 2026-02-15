#include <bits/stdc++.h>
using namespace std;
#define ll long long
 

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    ll n, k;
    cin >> n >> k;

    vector<ll> a(n), b(n);
    for (auto& x : a) cin >> x;
    for (auto& x : b) cin >> x;

    ll l = 0, r = 1e13;
    while (l < r) {
        ll mid = l + (r-l+1)/2;

        ll cookies = 0;
        for (int i = 0; i < n; i++) cookies += max(0LL, mid*a[i]-b[i]);

        if (cookies <= k) l = mid;
        else r = mid-1;
    }

    cout << l;
}