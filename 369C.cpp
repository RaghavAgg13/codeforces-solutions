#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n,m,a,b,c;
vector<vector<pair<int, int>>> adj;
vector<int> lv;

bool check(int x, int p, bool problem_road) {
    bool subtree_check = false;

    for (auto [y,c] : adj[x]) {
        if (y == p) continue;
        
        bool child_check = check(y, x, c==2);
        if (child_check) subtree_check = true;
    }

    if (!subtree_check && problem_road) {
        lv.push_back(x);
        return true;
    }
    return subtree_check || problem_road;

}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    adj.assign(n+1, vector<pair<int, int>>());
    
    m = n; while (--m) {
        cin >> a >> b >> c;
        adj[a].push_back({b,c});
        adj[b].push_back({a,c});
    }

    check(1, -1, false);

    cout << lv.size() << '\n';
    for (auto x : lv) cout << x << ' ';
}