#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    string seq;
    cin >> seq;

    int stack[seq.length()+1];
    int top = 0; 
    stack[top++] = -1;
    
    int cur = 0, cnt = 1, max = 0;

    for (int i = 0; i < seq.length(); i++) {
        if (seq[i] == '(') {
            stack[top++] = i;
        }
        else {
            if (top > 1) {
                top--;
                cur = i - stack[top-1];
                
                if (cur == max) cnt++;
                else if (cur > max) {
                    max = cur;
                    cnt = 1;
                }
            }
            else {
                stack[top-1] = i;
            }
        }
        // cout << "current cur, max " << cur << ',' << max << endl;
    }
    cout << max << ' ' << cnt << endl;
}