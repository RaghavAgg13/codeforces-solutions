#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int MOD = 1e9+7;

int t,n,l,r;
vector<ll> ans, memo;
vector<int> parent;

ll get_e(int i, vector<vector<int>>& tree) {
    if (memo[i] != -1) return memo[i];

    if (tree[i][0] == 0 && tree[i][1] == 0) return memo[i] = 1;

    ll l = get_e(tree[i][0], tree);
    ll r = get_e(tree[i][1], tree);

    return memo[i] = (l+r+3)%MOD;
}

ll ifs(int i, vector<vector<int>>& tree) {
    if (i == 0) return 0;
    if (ans[i] != -1) return ans[i];

    ll escape_t = get_e(i, tree);
    ll parent_t = ifs(parent[i], tree);

    return ans[i] = (escape_t+parent_t)%MOD;
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;

        vector<vector<int>> tree(n+1, vector<int>(2,0));
        parent.assign(n+1, 0);
        
        tree[0] = {1, 0};
        parent[1] = 0;

        for (int i = 1; i <= n; i++) {
            cin >> l >> r;

            if (l != 0) {
                tree[i] = {l,r};
                parent[l] = i;
                parent[r] = i;
            }
        }
        
        ans.assign(n+1, -1);
        memo.assign(n+1, -1);

        vector<ll> result;
        for (int i = 1; i <= n; i++) {
            result.push_back(ifs(i, tree));
        }

        for (auto x : result) cout << x << ' ';
        cout << '\n';
    }
}