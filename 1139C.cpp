#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
#define ll long long
const int MOD = 1e9+7;
const int MAX = 1e6;

vector<ll> fact(MAX+1);
vector<ll> invFact(MAX+1);

int t,n,m,k,a,b,c;
vector<int> dsu;

ll pow(ll base, ll exp) {
    ll res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res*base) % MOD;
        base = (base*base)%MOD;
        exp /= 2;
    }
    return res;
}

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

    cin >> n >> k;
    dsu.assign(n+1, -1);
    
    m = n; while (--m) {
        cin >> a >> b >> c;
        if (!c) merge(a,b);
    }
    
    ll inv = pow(n,k);
    for (int i = 1; i <= n; i++) {
        if (dsu[i] < 0) {
            ll sz = -dsu[i];
            inv = (inv - pow(sz, k) + MOD)%MOD;
        }
    }

    cout << inv << '\n';
}