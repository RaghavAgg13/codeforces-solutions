#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int t,n,m,a,b;
vector<string> grid;

void solve() {
    cin >> n >> m;
    grid.resize(n);
    for (int i = 0; i < n; i++) cin >> grid[i];

    a = 0, b = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'G') a++;

            if (grid[i][j] == 'B') {
                for (int d = 0; d < 4; d++) {
                    int nx = i+dx[d], ny = j+dy[d];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                    if (grid[nx][ny] != '.') continue;
                    grid[nx][ny] = '#';
                }
            }
        }
    }

    queue<pair<int, int>> q;
    q.push({n-1, m-1});

    if (a == 0) {
        cout << "YES\n";
        return;
    }

    while (!q.empty()) {
        auto [x,y] = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x+dx[i], ny = y+dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (grid[nx][ny] == '#') continue;
            if (grid[nx][ny] == 'G') b++;
            if (grid[nx][ny] == 'B') {
                cout << "NO\n";
                return;
            }
            grid[nx][ny] = '#';
            
            q.push({nx, ny});
        }
    }

    if (a == b) cout << "YES\n";
    else cout << "NO\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        solve();
    }
}