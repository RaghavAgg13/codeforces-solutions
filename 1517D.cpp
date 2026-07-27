#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,k,a,b;
vector<vector<pair<int, int>>> adj;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;
    vector<vector<int>> ver(n-1, vector<int>(m)), hor(n, vector<int>(m-1));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m-1; j++) cin >> hor[i][j];
    }
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < m; j++) cin >> ver[i][j];
    }

    if (k%2) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) cout << "-1 ";
            cout << '\n';
        }
        return 0;
    }
    
    int steps = k/2;
    vector<vector<vector<int>>> dp(steps+1, vector<vector<int>>(n, vector<int>(m, 1e9)));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) dp[0][i][j] = 0;
    }

    for (int s = 1; s <= steps; s++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (j > 0) dp[s][i][j] = min(dp[s][i][j], dp[s-1][i][j-1]+hor[i][j-1]);
                if (j < m-1) dp[s][i][j] = min(dp[s][i][j], dp[s-1][i][j+1]+hor[i][j]);
                if (i > 0) dp[s][i][j] = min(dp[s][i][j], dp[s-1][i-1][j]+ver[i-1][j]);
                if (i < n-1) dp[s][i][j] = min(dp[s][i][j], dp[s-1][i+1][j]+ver[i][j]);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << 2*dp[steps][i][j] << ' ';
        cout << '\n';
    }
}