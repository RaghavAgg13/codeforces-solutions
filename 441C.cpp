#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,k,a,b;
queue<int> cells;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;

    for (int i = 0; i < n; i++) {
        if (i%2) {
            for (int j = 0; j < m; j++) {
                cells.push(i+1);
                cells.push(j+1);
            }
        }
        else {
            for (int j = m-1; j >= 0; j--) {
                cells.push(i+1);
                cells.push(j+1);
            }
        }
    }
    
    int tar = k-1;
    while (tar--) {
        cout << "2 ";
        a = 4; while (a--) {
            cout << cells.front() << ' ';
            cells.pop();
        }
        cout << '\n';
    }

    cout << cells.size()/2 << ' ';
    while (!cells.empty()) {
        cout << cells.front() << ' ';
        cells.pop();
    }
}