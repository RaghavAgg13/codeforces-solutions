#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int n,m,a,b;
vector<vector<int>> grid;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    grid.resize(n, vector<int>(m, 0));
    queue<pair<int, int>> q;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            if (s[j] == 'S') grid[i][j] = 1;
            else if (s[j] == 'W') {
                grid[i][j] = -1;
                q.push({i,j});
            }
        }
    }
    
    while (!q.empty()) {
        auto [x,y] = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x+dx[i], ny = y+dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            if (grid[nx][ny] == 1) {
                cout << "NO";
                return 0;
            }
            else if (grid[nx][ny] == 0) grid[nx][ny] = 2;
        }
    }

    cout << "YES\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!grid[i][j]) cout << '.';
            else if (grid[i][j] == 1) cout << "S";
            else if (grid[i][j] == -1) cout << "W";
            else cout << "D";
        }
        cout << '\n';
    }
}