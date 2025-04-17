import java.io.*;
import java.util.*;

class Node implements Comparable<Node>{
    int x;
    int y;
    int before;
    int score;

    public Node(int x, int y, int before, int score) {
        this.x = x;
        this.y = y;
        this.before = before;
        this.score = score;
    }

    @Override
    public int compareTo(Node o) {
        if (this.score == o.score) {
            return o.x - this.x;
        }
        return this.score - o.score;
    }
}

class Main {

    public static final int MAX_N = 6;
    public static final int MAX_V = 100;
    public static final int MAX_NUM = Integer.MAX_VALUE;

    public static int n, m;
    public static int ans = MAX_NUM;
    public static int[][] matrix;
    public static PriorityQueue<Node> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        init();

        for (int i = 0; i < m; i++) {
            ans = Math.min(ans, start(0, i));
        }

        System.out.println(ans);
    }

    public static int start(int x, int y) {
        pq.offer(new Node(x, y, MAX_NUM, matrix[0][y]));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            x = node.x;
            y = node.y;

            if (x == n - 1) {
                return node.score;
            }

            for (int i = -1; i <= 1; i++) {
                if (node.before == i) continue;

                int nx = x + 1;
                int ny = y + i;

                if (canGo(nx, ny)) {
                    pq.offer(new Node(nx, ny, i, node.score + matrix[nx][ny]));
                }
            }
        }

        return MAX_NUM;
    }

    public static boolean canGo(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        matrix = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }
}