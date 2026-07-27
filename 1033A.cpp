#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

int n,m,ax,ay,bx,by,cx,cy;
vector<vector<int>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    cin >> ax >> ay;
    cin >> bx >> by;
    cin >> cx >> cy;

    queue<pair<int, int>> q;
    q.push({bx,by});
    unordered_map<int, int> map;
    map[bx*n+by] = 1;

    while (!q.empty()) {
        auto [x,y] = q.front(); q.pop();

        if (x == cx && y == cy) {
            cout << "YES";
            return 0;
        }

        for (int i = -1; i < 2; i++) {
            for (int j = -1; j < 2; j++) {
                int nx = x+i, ny = y+j;
                if (nx < 1 || nx > n || ny < 1 || ny > n) continue;
                if (nx == ax || ny == ay || abs(nx-ax) == abs(ny-ay)) continue;
                if (map[nx*n+ny]) continue;
                map[nx*n+ny] = 1;

                q.push({nx, ny});
            }
        }
    }

    cout << "NO";
}