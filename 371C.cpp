#include <bits/stdc++.h>
using namespace std;
#define ll long long
 

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    string ch;
    cin >> ch;
    int n1 = 0, n2 = 0, n3 = 0;
    for (auto& it : ch) {
        if (it == 'B') n1++;
        else if (it == 'S') n2++;
        else n3++;
    }

    vector<ll> a(3), b(3);
    for (auto& x : a) cin >> x;
    for (auto& x : b) cin >> x;
 
    ll money;
    cin >> money;

    int made = 0;

    ll l = 0, r = 1e13;
    while (l < r) {
        ll mid = l + (r-l+1)/2;

        ll cost = max(0LL, mid*n1-a[0])*b[0] + max(0LL, mid*n2-a[1])*b[1] + max(0LL, mid*n3-a[2])*b[2];
        if (cost <= money) {
            l = mid;
        } else r = mid-1;
    }

 
    cout << l;
}