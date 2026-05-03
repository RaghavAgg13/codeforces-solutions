#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
 
int n,x,step,i,j,k;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> n;
    vector<vector<ll>> adj(n, vector<ll>(n));

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) cin >> adj[i][j];
    }

    vector<int> x(n);
    for (i = 0; i < n; i++) {
        cin >> x[i]; x[i]--;
    }

    vector<ll> ans(n);

    for (step = n-1; step >= 0; step--) {
        k = x[step];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (adj[i][k]+adj[k][j] < adj[i][j]) {
                    adj[i][j] = adj[i][k]+adj[k][j];
                }
            }
        }

        ll sum = 0;
        for (int i = step; i < n; i++) {
            for (int j = step; j < n; j++) {
                sum += adj[x[i]][x[j]];
            }
        }
        ans[step] = sum;
    }
    
    for (i = 0; i < n; i++) cout << ans[i] << ' ';
}