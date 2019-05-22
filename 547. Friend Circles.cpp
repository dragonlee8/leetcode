class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size(), res = 0;
        vector<bool> visited(n, false);
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (visited[i]) continue;
            q.push(i);
            while (!q.empty()) {
                int t = q.front(); q.pop();
                visited[t] = true;
                for (int j = 0; j < n; ++j) {
                    if (!M[t][j] || visited[j]) continue;
                    q.push(j);
                }
            }
            ++res;
        }
        return res;
    }
};
