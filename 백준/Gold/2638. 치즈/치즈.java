import java.util.*;

public class Main {

    static int n, m;
    static int[][] matrix;
    static boolean[][] visited;
    static Queue<int[]> queue = new ArrayDeque<>();
    static List<int[]> lists;
    static int time = 0;
    static int cnt = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        matrix = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int temp = sc.nextInt();
                matrix[i][j] = temp;
                if (temp == 1) cnt++;
            }
        }

        lists = new LinkedList<>();

        while (cnt > 0) {
            visited = new boolean[n][m];
            time++;

            BFS();

            while (lists.size() > 0) {
                int[] pos = lists.remove(0);
                if (matrix[pos[0]][pos[1]] == 0) continue;
                matrix[pos[0]][pos[1]] = 0;
                cnt--;
            }
        }

        System.out.println(time);
    }

    public static void BFS() {
        int[] dx = {0, 1, 0, -1};
        int[] dy = {-1, 0, 1, 0};
        queue.offer(new int[]{0, 0});
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int row = pos[0];
            int col = pos[1];

            for (int k = 0; k < 4; k++) {
                int nx = row + dx[k];
                int ny = col + dy[k];

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (matrix[nx][ny] == 0) {
                        // 방문한 경우
                        if (visited[nx][ny]) continue;
                        // 방문하지 않은 경우
                        queue.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;
                    } else if (matrix[nx][ny] == 1) {
                        // 방문한 경우
                        if (visited[nx][ny]) {
                            lists.add(new int[]{nx, ny});
                        }
                        // 방문하지 않은 경우
                        else if (!visited[nx][ny]) {
                            visited[nx][ny] = true;
                        }
                    }
                }
            }
        }
    }
}