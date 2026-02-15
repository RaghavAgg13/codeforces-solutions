#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    string seq;
    cin >> seq;

    char stack[seq.length()];
    int top = 0; 
    
    int cur = 0;

    for (int i = 0; i < seq.length(); i++) {
        if (seq[i] == '(') {
            stack[top++] = '(';
            cur++;
        }
        else {
            if (top > 0) {
                stack[top--];
                cur++;
            } else top = 0;
        }
    }
    cout << cur-top << endl;
}