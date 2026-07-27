#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int t,l,r,k;

int f(int x) {
    if (x < 10) return x;

    int prod = 1;
    while (x > 9) {
        if (x%10 != 0) prod *= (x%10);
        x /= 10;
    }
    prod *= x;
    
    return f(prod);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    vector<vector<int>> val(1000001, vector<int>(10, 0));
    for (int i = 1; i <= 1000000; i++) {
        for (int j = 1; j <= 9; j++) val[i][j] = val[i-1][j];

        val[i][f(i)]++;
    }

    cin >> t;
    while (t--) {
        cin >> l >> r >> k;
        cout << val[r][k]-val[l-1][k] << '\n';

    }
}