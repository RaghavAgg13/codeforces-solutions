#include <iostream>
#include <algorithm>
#include <vector>
#define ll long long
using namespace std;

int t,n,a,b,x,y;
vector<int> p,arr;

ll dfs(int root, ll moves) {
    ll max_score = 0, cur_score = 0;
    int curr = root;

    ll steps = min((ll)n, moves);
    for (int i = 0; i < steps; i++) {
        max_score = max(max_score, cur_score+moves*arr[curr]);
        cur_score += arr[curr];
        
        moves--;
        curr = p[curr];
    }

    return max_score;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        ll k;
        cin >> n >> k >> x >> y;
        p.resize(n+1);
        arr.resize(n+1);

        for (int i = 1; i <= n; i++) cin >> p[i];
        for (int i = 1; i <= n; i++) cin >> arr[i];

        ll n1 = dfs(x, k), n2 = dfs(y, k);

        if (n1 > n2) cout << "Bodya\n";
        else if (n1 < n2) cout << "Sasha\n";
        else cout << "Draw\n";
    }
}