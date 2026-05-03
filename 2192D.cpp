#include <bits/stdc++.h>
using namespace std;
#define ll long long

int t,n,l,r,i;

typedef struct Node {
    int val;
    vector<int> children;
} Node;

Node* create_node(int val) {
    Node* node = new Node;
    node->val = val;
    node->children.clear();

    return node;
}

int main(void) {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> n;

        vector<Node*> tree(n+1);
        for (int i = 1; i <= n; i++) {
            cin >> l;
            tree[i] = create_node(l);
        }

        for (i = 0; i < n-1; i++) {
            cin >> l >> r;
            tree[l]->children.push_back(r);
            tree[r]->children.push_back(l);
        }
        
    }
}