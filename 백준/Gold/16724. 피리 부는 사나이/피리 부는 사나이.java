import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

class Pair {
    int x;
    int y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Main {
    static final int MAX_ROW = 1000;
    static final int MAX_COL = 1000;

    static int[][] dir = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};

    static int n, m, ans, minusAns;
    static char[][] matrix = new char[MAX_ROW][MAX_COL];
    static int[][] visited = new int[MAX_ROW][MAX_COL];
    static Deque<Pair> dq = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        init();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] == 0) {
                    bfs(new Pair(i, j));
                }
            }
        }

        System.out.println(ans - minusAns);
    }

    public static void bfs(Pair p) {
        dq.offer(p);
        visited[p.x][p.y] = ++ans;

        while (!dq.isEmpty()) {
            p = dq.poll();
            int x = p.x;
            int y = p.y;

            int dirNum = -1;
            switch (matrix[p.x][p.y]) {
                case 'D':
                    dirNum = 0;
                    break;
                case 'L':
                    dirNum = 1;
                    break;
                case 'U':
                    dirNum = 2;
                    break;
                case 'R':
                    dirNum = 3;
                    break;
            }

            int nx = x + dir[dirNum][0];
            int ny = y + dir[dirNum][1];

            if (inRange(nx, ny)) {
                if (visited[nx][ny] == 0) {
                    // 미방문 지역
                    dq.offer(new Pair(nx, ny));
                    visited[nx][ny] = ans;
                } else if (visited[nx][ny] == ans) {
                    // 현재 방문한 지역 => 새로운 safe 존 필요
                    dq.clear();
                    return;
                } else {
                    minusAns++;
                    dq.clear();
                    return;
                    // 과거에 방문한 지역. 기존 safe 존으로 갈 예정.
                }
            }
        }
    }

    public static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < m; j++) {
                matrix[i][j] = str.charAt(j);
            }
        }
    }
}