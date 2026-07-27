#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long

int n,a,b;
string s;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    vector<int> a(n);
    for (auto &x : a) cin >> x;
    
    cin >> s; s = " "+s;

    int start = 0;
    vector<int> arr = {a[0]};
    for (int i = 1; i < n; i++) {
        if (s[i] == '1') arr.push_back(a[i]);
        else {
            sort(arr.begin(), arr.end());

            int j = start;
            for (auto x : arr) a[j++] = x;
            start = i;
            arr = {a[i]};
        }
    }

    sort(arr.begin(), arr.end());

    int j = start;
    for (auto x : arr) a[j++] = x;

    for (int i = 1; i < n; i++) {
        if (a[i] < a[i-1]) {
            cout << "NO";
            return 0;
        }
    }
    cout << "YES";
}