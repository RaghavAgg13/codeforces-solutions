#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;
#define ll long long

int dx[] = {0,0,1,-1,1,-1,1,-1};
int dy[] = {-1,1,0,0,1,1,-1,-1};

int t;
ll n,m,b;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;
        m = n+1;

        queue<pair<ll, ll>> q;
        unordered_map<ll, int> map;

        auto key = [&](ll x, ll y) {
            return ((x+m+2)<<32) | (y+m+2);
        };

        b = 0;
        q.push({n,0});
        map[key(n,0)] = 1;

        while (!q.empty()) {
            auto [x,y] = q.front(); q.pop();
            if (n*n <= x*x+y*y && x*x+y*y < m*m) b++;
            
            for (int i = 0; i < 8; i++) {
                ll nx = x+dx[i], ny = y+dy[i];
                ll d = nx*nx + ny*ny;
                
                if (d < n*n || d >= m*m) continue;
                if (map[key(nx,ny)]) continue; map[key(nx,ny)] = 1;

                q.push({nx,ny});
            }
        }
        cout << b << '\n';    
    }
}