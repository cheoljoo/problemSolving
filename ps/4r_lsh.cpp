// saehoo lee
#include <iostream>
#include <vector>
using namespace std;
 
int dfs(vector<vector<int>>& graph, vector<bool>& dominating, vector<bool>& dominated, vector<bool>& visited, int here) {
    int ret = 0;
    visited[here] = true;
    if (graph[here].size() > 0) {
        bool needDominating = false;
        for (auto there : graph[here]) {
            if (visited[there]) continue;
            ret += dfs(graph, dominating, dominated, visited, there);
            if (dominating[there]) {
                dominated[here] = true;
                continue;
            }
            if (!dominated[there]) {
                needDominating = true;
                dominated[there] = true;
            }
        }
        if (needDominating) {
            dominated[here] = dominating[here] = true;
            ret++;
        }
    }
    return ret;
}
int main() {
    ios::sync_with_stdio(false);
    int C;
    cin >> C;
    for (int c = 1; c <= C; c++) {
        int G, H;
        cin >> G >> H;
        vector<vector<int>> graph(G, vector<int>());
        for (int i = 0; i < H; i++) {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        vector<bool> dominating(G, false);
        vector<bool> dominated(G, false);
        vector<bool> visited(G, false);
        int ans = 0;
        for (int i = 0; i < G; i++) {
            if (visited[i] == false) {
                ans += dfs(graph, dominating, dominated, visited, i);
                if (!dominated[i]) {
                    ans++;
                }
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
