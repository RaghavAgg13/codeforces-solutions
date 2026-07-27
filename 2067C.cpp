#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#define ll long long
using namespace std;

int t,n,m,a,b;

bool check(ll x) {
    while (x > 0) {
        if (x%10 == 7) return true;
        x /= 10;
    }
    return false;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> t;
    while (t--) {
        cin >> n;
        
        if (check(n)) {
            cout << 0 << '\n';
            continue;
        }
        
        queue<pair<int, pair<ll, ll>>> q;

        ll y = 9;
        while (y < 9999999999LL) {
            q.push({0, {n, y}});
            y = y*10+9;
        }

        while (!q.empty()) {
            auto [mov,state] = q.front(); q.pop();
            auto [x,start_y] = state;

            if (mov > 7) continue;

            if (check(x)) {
                cout << mov << '\n';
                break;
            }

            ll y = start_y;
            if (mov+1 > 7) continue;
            q.push({mov+1, {x+y, y}});
        }
    }
    
}