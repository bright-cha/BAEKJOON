import java.util.*;

class Solution {
    public static final int MAX_N = 200;
    public static int cnt;
    public static boolean[] visited = new boolean[MAX_N];
    public static Deque<Integer> dq = new ArrayDeque<>();
    
    public int solution(int n, int[][] computers) {
        for (int i = 0; i < n; i++) {
            if (!visited[i])
                cnt++;
                bfs(i, n, computers);
        }
        return cnt;
    }
    
    public static void bfs(int cur, int n, int[][] computers) {
        dq.add(cur);
        visited[cur] = true;
        
        while (!dq.isEmpty()) {
            cur = dq.poll();
            
            for (int i = 0; i < n; i++) {
                if (computers[cur][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    dq.add(i);
                }
            }
        }
    }
}