#include <iostream>
#include <algorithm>
#include <vector>
#define ll long long
using namespace std;

ll n,a;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    vector<ll> arr(n);
    vector<vector<int>> thr(n, vector<int>(3, 0));

    for (auto &x : arr) cin >> x;
    for (int i = 0; i < n; i++) thr[i][2] = i;
    
    for (int i = 0; i < n; i++) {
        a = arr[i];
        while (a%3 == 0) {
            thr[i][0]--;
            a /= 3;
        }
        
        while (a%2 == 0) {
            thr[i][1]++;
            a /= 2;
        }
    }
    
    sort(thr.begin(), thr.end());

    for (auto x : thr) cout << arr[x[2]] << ' ';
}