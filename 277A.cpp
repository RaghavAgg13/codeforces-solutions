#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int n,m,a,b,cnt,zeros;
vector<int> parent, lang;

int find(int a) {
    while (parent[a] >= 0) {
        if (parent[parent[a]] >= 0) parent[a] = parent[parent[a]];
        a = parent[a];
    }

    return a;
}

void merge(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;

    if (parent[a] <= parent[b]) {
        parent[a] += parent[b];
        parent[b] = a;
    }
    else {
        parent[b] += parent[a];
        parent[a] = b;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    parent.assign(n+1, -1);
    lang.assign(m+1, -1);
    cnt = n; zeros = 0;

    for (int i = 1; i <= n; i++) {
        cin >> a;
        if (a == 0) zeros++;

        while (a--) {
            cin >> b;

            if (lang[b] == -1) lang[b] = i;
            else if (find(lang[b]) != find(i)){
                merge(lang[b], i);
                cnt--;
            }
        }
    }

    if (zeros == n) cnt = n+1;
    cout << cnt-1 << '\n';
}