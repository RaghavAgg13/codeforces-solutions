#include <bits/stdc++.h>
using namespace std;

int main(void) {
    #define int long long
    int n;
    cin >> n;

    while (n--) {
        int s,k,m;
        cin >> s >> k >> m;

        int rem;
        if (s <= k) rem = max(0LL, s-m%k);
        else {
            if (!(m/k)%2) rem = s-m%k;
            else rem = k-m%k;
        }
        cout << rem << '\n';
    }
    return 0;
}
