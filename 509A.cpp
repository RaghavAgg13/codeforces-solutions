#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> a(n);
    int top = 0;
    for (int i = 0; i < n; i++) a[top++] = 1;

    for (int i = 0; i < n-1; i++) {
        for (int i = 1; i < n; i++) a[i] += a[i-1];        
        
    }
    cout << a[n-1] << endl;
}