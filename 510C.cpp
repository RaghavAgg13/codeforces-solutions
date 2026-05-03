#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define ll long long

int n,m,a,b,c;

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    vector<string> words(n);
    for (int i = 0; i < n; i++) cin >> words[i];
    
    vector<vector<int>> adj(26); 
    vector<int> degree(26, 0);


    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            int len = min(words[i].length(), words[j].length());
            bool found_diff = false;
            for (int k = 0; k < len; k++) {
                if (words[i][k] != words[j][k]) {
                    adj[words[i][k]-'a'].push_back(words[j][k]-'a');
                    degree[words[j][k]-'a']++;
                    found_diff = true;
                    break;
                }
            }
            if (!found_diff && words[i].length() > words[j].length()) {
                cout << "Impossible";
                return 0;
            }
        }
    }

    string top = "";
    queue<int> Q;
    for (int i = 0; i < 26; i++) {
        if (!degree[i]) Q.push(i);
    }


    while (!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        top.push_back(cur+'a');

        for (auto x : adj[cur]) {
            if (--degree[x] == 0) Q.push(x);
        }
    }

    if (top.size() == 26) cout << top;
    else cout << "Impossible";
}