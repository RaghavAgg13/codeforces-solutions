#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
string str;
vector<vector<int>> grid, color;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

void map(int x, int y, int c) {
    color[x][y] = c;

    for (int i = 0; i < 4; i++) { 
        int nx = x+dx[i], ny = y+dy[i];

        if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
        if (color[nx][ny] != -1) continue;
        
        map(nx, ny, -c);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    grid.assign(n, vector<int>(m));
    color.assign(n, vector<int>(m, -1));
    
    for (int i = 0; i < n; i++) {
        cin >> str;
        for (int j = 0; j < m; j++) {
            if (str[j] == '.') grid[i][j] == 1;
            else {
                grid[i][j] = 0;
                color[i][j] = 0;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (color[i][j] == -1) map(i, j, 2);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (color[i][j] == 0) cout << "-";
            else if (color[i][j] == 2) cout << "W";
            else cout << "B";
        }
        cout << '\n';
    }
}