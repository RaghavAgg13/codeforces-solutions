#include <bits/stdc++.h>
using namespace std;
 
int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
 
    int n;
    cin >> n;
    int stack[30], top = 0;
 
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j < 2*(n-i); j++) cout << " ";

        for (int j = 0; j <= i; j++) {
            cout << j;
            stack[top++] = j;
            if (j < i) cout << ' ';
        }

        top--;
        if (i) cout << ' ';
        while (top) {
            cout << stack[--top];
            if (top) cout << ' ';
        }
        cout << endl;
    }
    
    for (int i = n-1; i >= 0; i--) {
        for (int j = 0; j < 2*(n-i); j++) cout << " ";

        for (int j = 0; j <= i; j++) {
            cout << j;
            stack[top++] = j;
            if (j < i) cout << ' ';
        }

        top--;
        if (i) cout << ' ';
        while (top) {
            cout << stack[--top];
            if (top) cout << ' ';
        }
        cout << endl;
    }
}