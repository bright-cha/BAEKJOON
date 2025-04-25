import java.io.*;
import java.util.*;

class Node {
    int x;
    int y;
    int score;
    char pre;

    public Node(int x, int y, int score, char pre) {
        this.x = x;
        this.y = y;
        this.score = score;
        this.pre = pre;
    }
}

class Main {

    // 학교에서 집으로 가는 경로에서 만나는 숫자와 연산자의 연산 결과의 최댓값과 최솟값을 구하려고 한다
    // 항상 자신의 집 (1, 1)에서 학교 (N, N)까지 최단거리로 이동 and 오른쪽과 아래로만 이동

    public static int n;
    public static Character[][] matrix;
    public static int min = Integer.MAX_VALUE;
    public static int max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        init();

        bfs();

        System.out.println(max + " " + min);
    }

    public static void bfs() {
        Deque<Node> dq = new ArrayDeque<>();
        dq.addLast(new Node(0, 0, Character.getNumericValue(matrix[0][0]), ' '));

        int[][] delta = {{0, 1}, {1, 0}};

        while (!dq.isEmpty()) {
            Node node = dq.removeFirst();
            int x = node.x;
            int y = node.y;
            int score = node.score;
            char pre = node.pre;

            if (x == n - 1 && y == n - 1) {
                max = Math.max(max, score);
                min = Math.min(min, score);
                continue;
            }

            for (int[] n : delta) {
                int nx = x + n[0];
                int ny = y + n[1];

                if (canGo(nx, ny)) {

                    if (Character.isDigit(matrix[nx][ny])) {
                        dq.addLast(new Node(nx, ny, calculate(nx, ny, score, pre), pre));
                    } else {
                        dq.addLast(new Node(nx, ny, score, matrix[nx][ny]));
                    }
                }
            }
        }
    }

    public static int calculate(int x, int y, int score, char pre) {
        switch (pre) {
            case '+':
                return score + Character.getNumericValue(matrix[x][y]);
            case '-':
                return score - Character.getNumericValue(matrix[x][y]);
            case '*':
                return score * Character.getNumericValue(matrix[x][y]);
        }
        return 0;
    }

    public static boolean canGo(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < n;
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        matrix = new Character[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                matrix[i][j] = st.nextToken().charAt(0);
            }
        }
    }
}