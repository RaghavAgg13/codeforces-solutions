#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;

    queue<int> x,y;
    
    cin >> a; while (a--) {
        cin >> b;
        x.push(b);
    }

    cin >> a; while (a--) {
        cin >> b;
        y.push(b);
    }
    
    int cnt = 0;
    while (cnt < 150) {
        cnt++;

        a = x.front(); b = y.front();
        x.pop(); y.pop();

        if (a > b) {
            x.push(b); x.push(a);
        }
        else {
            y.push(a); y.push(b);
        }

        if (y.empty() || x.empty()) break;
    }

    if (cnt == 150) cout << "-1\n";
    else if (y.empty()) cout << cnt << " 1\n";
    else cout << cnt << " 2\n";
}