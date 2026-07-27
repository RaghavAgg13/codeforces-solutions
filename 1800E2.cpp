#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
using namespace std;
#define ll long long

int x,n,k,a,b;
string s,t;
vector<int> dsu;
set<int> par;
vector<vector<int>> grps;

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

    cin >> x;
    while (x--) {
        cin >> n >> k;
        dsu.assign(n+1, -1);
        
        cin >> s;
        cin >> t;

        for (int i = 0; i < n-k; i++) {
            merge(i, i+k);
            if (i+k+1 < n) merge(i, i+k+1);
        }
    
        grps.assign(n+1, vector<int>());
        par.clear();
        
        for (int i = 0; i < n; i++) {
            grps[find(i)].push_back(i);
            par.insert(find(i));
        }
        
        bool valid = true;
        for (auto p : par) {
            int freq[26] = {0};

            for (auto val : grps[p]) {
                freq[s[val]-'a']++;
                freq[t[val]-'a']--;
            }

            for (int i = 0; i < 26; i++) {
                if (freq[i] != 0) {
                    valid = false;
                    break;
                }
            }

            if (!valid) break;
        }

        if (valid) cout << "YES\n";
        else cout << "NO\n";
    }   
}