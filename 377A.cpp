#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,k,a,b;
string s;
vector<vector<int>> grid;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;
    grid.assign(n, vector<int>(m, 0));

    int S = n*m-k;
    pair<int, int> emt = {-1, -1};
    for (int i = 0; i < n; i++) {
        cin >> s;
        for (int j = 0; j < m; j++) {
            if (s[j] == '#') {
                grid[i][j] = -1;
                S--;
            }
            else if (emt.first == -1) emt = {i,j};
        }
    }

    queue<pair<int, int>> q;
    q.push(emt);

    while (!q.empty()) {
        auto [x,y] = q.front(); q.pop();

        if (grid[x][y] != 0) continue; grid[x][y] = 1;
        if (--S == 0) break;

        for (int i = 0; i < 4; i++) {
            int nx = x+dx[i], ny = y+dy[i];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            if (grid[nx][ny] == -1) continue;

            q.push({nx, ny});
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == -1) cout << '#';
            else if (grid[i][j] == 0) cout << "X";
            else cout << ".";
        }
        cout << '\n';
    }
}