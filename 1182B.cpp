#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int n,m,a,b;
vector<string> s;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    a = 0; b = 0;
    pair<int, int> center = {-1, -1};

    for (int i = 0; i < n; i++) {
        string st; cin >> st;
        s.push_back(st);
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (s[i][j] == '*') a++;
            if (!(0 < i && i+1 < n && 0 < j && j+1 < m)) continue;

            if (s[i][j] == '*' && s[i+1][j] == '*' && s[i-1][j] == '*' && s[i][j+1] == '*' && s[i][j-1] == '*') {
                if (center.first != -1 && center.second != -1) {
                    cout << "NO";
                    return 0;
                }

                center = {i, j};
            }
        }
    }

    if (center.first == -1) {
        cout << "NO";
        return 0;
    }

    for (int i = center.first-1; i >= 0; i--) {
        if (s[i][center.second] == '*') a--;
        else break;
    }
    
    for (int i = center.first+1; i < n; i++) {
        if (s[i][center.second] == '*') a--;
        else break;
    }

    for (int j = center.second-1; j >= 0; j--) {
        if (s[center.first][j] == '*') a--;
        else break;
    }

    for (int j = center.second+1; j < m; j++) {
        if (s[center.first][j] == '*') a--;
        else break;
    }

    if (a == 1) cout << "YES";
    else cout << "NO";
}