#include <bits/stdc++.h>
using namespace std;
#define ll long long

int sum_digits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n%10;
        n /= 10;
    }
    return sum;
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int n;
    cin >> n;
    map<int, int> valid_pairs;

    for (int k = 0; k < n; k++) {
        string a;
        cin >> a;
        int len = a.length(), top = 0;
        vector<int> stack(len);

        int f = 0;
        for (int i = 0; i < len; i++) {
            if (a[i] == '(') {
                stack[top++] = a[i];
                f++;
            }
            else {
                f--;
                if (top > 0 && stack[top-1] == '(') top--;
                else stack[top++] = ')';
            }
        }

        bool check = true;
        for (int i = 0; i < top-1; i++) {
            if (stack[i] != stack[i+1]) check = false;
        }

        if (check) valid_pairs[f]++;
    }

    int cnt = 0;
    for (auto &x : valid_pairs) {
        int key = x.first, value = x.second;

        if (valid_pairs.count(-key)) {
            int second_val = valid_pairs[-key];

            int del;
            if (key == 0) del = value / 2;
            else del = min(value, second_val);

            cnt += del;
            valid_pairs[key] -= del;
            valid_pairs[-key] -= del;
        }
    }

    cout << cnt << endl;
}