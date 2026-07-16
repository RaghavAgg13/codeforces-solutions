#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m,a,b;
vector<int> parent, arr;

int get(int i) {
    if (i == -1) return 0;
    if (arr[i] != 0) return arr[i];

    return arr[i] = get(parent[i])+1;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    parent.assign(n+1, -1); arr.assign(n+1, 0);
    for (int i = 1; i <= n; i++) cin >> parent[i];

    int ans = 0;
    for (int i = 1; i <= n; i++) {
        ans = max(ans, get(i));
    }

    cout << ans << '\n';
}