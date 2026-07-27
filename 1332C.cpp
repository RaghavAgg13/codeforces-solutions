#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
using namespace std;

int t,n,k,a,b;
string s;
vector<int> dsu;

int find(int x) {
    if (dsu[x] < 0) return x;
    return dsu[x] = find(dsu[x]);
}

void merge(int x, int y) {
    x = find(x);
    y = find(y);

    if (x == y) return;

    if (dsu[x] <= dsu[y]) {
        dsu[x] += dsu[y];
        dsu[y] = x;
    } else {
        dsu[y] += dsu[x];
        dsu[x] = y;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n >> k;
        cin >> s;

        dsu.assign(n+1, -1);
        
        for (int i = 0; i < n-k; i++) merge(i, k+i);
        for (int i = 0; i < n/2; i++) merge(i, n-1-i);
        
        vector<vector<int>> grps(n+1, vector<int>());
        set<int> par;
        for (int i = 0; i < n; i++) {
            grps[find(i)].push_back(s[i]-'a');
            par.insert(find(i));
        }

        int cost = 0;
        for (auto p : par) {
            int freq[26] = {0}, idx = 0;

            for (auto x : grps[p]) {
                if (++freq[x] > freq[idx]) idx = x;
            }

            for (int i = 0; i < 26; i++) {
                if (i != idx) cost += freq[i];
            }
        }

        cout << cost << '\n';
    }
}