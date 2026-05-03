#include <iostream>
#include <vector>
using namespace std;
#define ll long long
 
int n,m;
char x,y;
 
int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    string a;
    cin >> a;

    vector<int> hash(26);
    for (int i = 0; i < 26; i++) hash[i] = i;

    vector<vector<int>> keys(26);
    for (int i = 0; i < n; i++) keys[a[i]-'a'].push_back(i);

    while (m--) {
        cin >> x >> y;

        swap(hash[x-'a'], hash[y-'a']);
    }

    vector<char> ans(n);
    for (int i = 0; i < 26; i++) {
        for (auto j : keys[hash[i]]) {
            ans[j] = i+'a';
        }
    }
    for (auto x : ans) cout << x;

}