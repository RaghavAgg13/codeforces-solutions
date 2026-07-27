#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int n,m,a,b;
string s;
vector<int> dsu,freq;

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

    cin >> n;
    dsu.assign(n, -1);
    freq.assign(26, -1);
    
    for (int i = 0; i < n; i++) {
        cin >> s;
        for (int j = 0; j < s.size(); j++) {
            if (freq[s[j]-'a'] == -1) {
                freq[s[j]-'a'] = i;
                continue;
            }

            merge(freq[s[j]-'a'], i);
        }
    }

    b = 0;
    for (int i = 0; i < n; i++) {
        if (dsu[i] < 0) b += 1;
    }

    cout << b;
}