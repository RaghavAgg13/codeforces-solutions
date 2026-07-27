#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

int n,m,a,b;
vector<vector<int>> grid;

int dx[] = {0,1,0,-1};
int dy[] = {-1,0,1,0};

void solve(int pos, int val, int cnt) {
    stack<pair<int, int>> s;
    s.push({pos, pos});

    while (cnt > 0) {
        auto [x,y] = s.top();
        bool moved = false;

        for (int i = 0; i < 4; i++) {
            int nx = x+dx[i], ny = y+dy[i];
            if (nx <= 0 || nx > n || ny <= 0 || ny > nx) continue;
            if (grid[nx][ny]) continue;
            
            grid[nx][ny] = val;
            cnt--;
            s.push({nx, ny});
            moved = true;
            break;
        }

        if (!moved) s.pop();
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    grid.assign(n+1, vector<int>(n+1, 0));

    for (int i = 1; i <= n; i++) {
        cin >> a;
        grid[i][i] = a;
    }

    for (int i = 1; i <= n; i++) solve(i, grid[i][i], grid[i][i]-1);
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << grid[i][j] << ' '; 
        }
        cout << '\n';
    }
}